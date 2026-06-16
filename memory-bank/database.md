# THIẾT KẾ CƠ SỞ DỮ LIỆU (DATABASE SCHEMA & DESIGN)

Dự án **Phàm Nhân** chuyển sang sử dụng PostgreSQL làm cơ sở dữ liệu quan hệ chính qua **Prisma ORM**, cùng với Redis để phục vụ cho các bảng xếp hạng (Leaderboards) thời gian thực.

---

## 1. THIẾT KẾ SCHEMA PRISMA (`schema.prisma` cho PostgreSQL)

Dưới đây là cấu trúc các bảng dữ liệu được định nghĩa bằng Prisma Schema:

```prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

// --- Bảng Người Chơi ---
model User {
  id               String      @id @default(uuid())
  username         String      @unique
  email            String      @unique
  passwordHash     String      // Mật khẩu mã hóa
  tuVi             BigInt      @default(0)     // Điểm tu vi tích lũy (BigInt để tránh tràn số khi tu luyện nghìn năm)
  realm            String      @default("PHAM_NHAN") // Cảnh giới hiện tại
  spiritStones     BigInt      @default(0)     // Linh thạch sở hữu
  cultivationPath  String?     // Đường tu hành đã chọn: DAO_TU, THE_TU, MA_TU, hoặc null
  
  // Chỉ số Sinh tồn & Thọ nguyên
  age              Int         @default(18)    // Tuổi nhân vật hiện tại
  maxAge           Int         @default(100)   // Giới hạn tuổi thọ cảnh giới (Thọ nguyên)
  lineagePoints    Int         @default(0)     // Điểm Chân Linh tích lũy sau luân hồi
  reincarnationCnt Int         @default(0)     // Số lần luân hồi chuyển thế
  
  // Thời gian
  lastCultivatedAt DateTime    @default(now()) // Lần cuối cập nhật tĩnh tọa
  createdAt        DateTime    @default(now())
  updatedAt        DateTime    @updatedAt

  // Quan hệ
  inventories      Inventory[]
  encounters       Encounter[]
  linhMachs        ActiveLinhMach[]
  abodePlot        AbodePlot?

  @@index([tuVi(sort: Desc)])
}

// --- Bảng Túi Đồ ---
model Inventory {
  id        String   @id @default(uuid())
  userId    String
  itemId    String   // ID của vật phẩm (ví dụ: "item_truc_co_dan", "item_khien_ty_loi")
  quantity  Int      @default(1)
  updatedAt DateTime @updatedAt

  // Quan hệ
  user      User     @relation(fields: [userId], references: [id], onDelete: Cascade)

  @@unique([userId, itemId]) // Tránh trùng lặp vật phẩm của một người chơi
}

// --- Bảng Lịch Sử Kỳ Ngộ ---
model Encounter {
  id            String   @id @default(uuid())
  userId        String
  encounterType String   // Loại kỳ ngộ ngẫu nhiên gặp phải
  resolved      Boolean  @default(false) // Đã giải quyết (chọn phương án) chưa
  choiceMade    Int?     // Lựa chọn đã bấm (0, 1, 2)
  rewardsLog    String?  // Ghi nhật ký phần thưởng nhận được dạng JSON string
  createdAt     DateTime @default(now())

  // Quan hệ
  user          User     @relation(fields: [userId], references: [id], onDelete: Cascade)

  @@index([userId, createdAt(sort: Desc)])
}

// --- Bảng Chiếm Giữ Linh Mạch ---
model ActiveLinhMach {
  id          String   @id @default(uuid())
  userId      String   @unique
  linhMachId  String   // Định danh mỏ linh thạch (ví dụ: "mỏ_cực_phẩm_01")
  occupiedAt  DateTime @default(now())
  expiresAt   DateTime // Thời điểm hết hạn chiếm giữ (Tối đa 4 giờ)

  // Quan hệ
  user        User     @relation(fields: [userId], references: [id], onDelete: Cascade)

  @@index([linhMachId])
}

// --- Bảng Ô Động Phủ Phân Tầng ---
model AbodePlot {
  id            String   @id @default(uuid())
  userId        String   @unique // Một người chỉ sở hữu tối đa 1 ô đất tại một thời điểm
  floor         Int      // Tầng tháp động phủ (1, 2, 3...)
  plotIndex     Int      // Vị trí ô trong tầng (từ 1 đến 100)
  purchasePrice BigInt   // Số tiền linh thạch đã dùng để mua ô đất
  createdAt     DateTime @default(now())
  updatedAt     DateTime @updatedAt

  // Quan hệ
  user          User     @relation(fields: [userId], references: [id], onDelete: Cascade)

  @@unique([floor, plotIndex]) // Mỗi ô đất tại một tầng chỉ có tối đa 1 người sở hữu
}
```

---

## 2. KIẾN TRÚC CACHING VÀ LEADERBOARD TRONG REDIS

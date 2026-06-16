# KIẾN TRÚC HỆ THỐNG (SYSTEM ARCHITECTURE)

Tài liệu này mô tả cấu trúc thư mục, các lớp dịch vụ (layer) và luồng hoạt động chính của hệ thống game **Phàm Nhân** sử dụng WebSockets truyền tin nhị phân và Prisma ORM.

---

## 1. TECH STACK (CÔNG NGHỆ SỬ DỤNG)
* **Frontend Runtime & Framework**: React.js (Vite) + Tailwind CSS (Styling) + Zustand (State management).
* **Backend Runtime**: Node.js (v18+).
* **Framework Backend**: Express.js (HTTP server để setup và serve frontend static) + `ws` (WebSocket Server).
* **Database**: PostgreSQL (lưu trữ thông tin người chơi qua **Prisma ORM**) & Redis (quản lý bảng xếp hạng `ZSET`).
* **Binary Serialization**: Protocol Buffers (Protobuf) thông qua thư viện `protobufjs` để đóng gói/giải mã các gói tin nhị phân trên WebSocket.
* **Production**: Docker (Dockerfile cho FE & BE) + Docker Compose.

---

## 2. CẤU TRÚC DỰ ÁN KHI ĐÓNG GÓI DOCKER
Hệ thống được tách biệt thành 2 thư mục chính độc lập để đóng gói vào Container:

```
phamnhan/
├── backend/            # Code Backend (Express, Prisma, WS Server)
│   ├── prisma/         # Cấu hình Prisma schema và migrations
│   ├── src/            # Mã nguồn backend
│   └── Dockerfile      # Đóng gói backend runner
├── frontend/           # Code Frontend (React, Zustand, WS Client)
│   ├── src/            # Mã nguồn frontend
│   └── Dockerfile      # Đóng gói frontend build Nginx
├── docker-compose.yml  # File liên kết Postgres, Redis, BE, FE
└── game-design.md      # Tài liệu thiết kế trò chơi chi tiết
```

---

## 3. LUỒNG DỮ LIỆU THỜI GIAN THỰC (REAL-TIME DATA FLOW)

Mọi tương tác trong game không đi qua REST API thông thường mà được xử lý qua socket với cơ chế truyền tin nhị phân:

```
[React View] ──► Trigger Action (ví dụ: Đột phá)
      │
      ▼ (Zustand / hook useWebSocket)
[ProtoService] ──► Encode JSON sang Protobuf binary + Thêm 2-byte Opcode
      │
      ▼ (WebSocket connection)
[Backend WebSocket Server] ──► Đọc Opcode, phân phối tới handler thích hợp
      │
      ├─► [authHandler.js]       (Xác thực phiên)
      ├─► [cultivationHandler.js](Xử lý tăng tu vi, tính toán lôi kiếp đột phá)
      ├─► [abodeHandler.js]      (Trồng trọt linh dược, khai khoáng linh mạch)
      └─► [encounterHandler.js]  (Kích hoạt kỳ ngộ, lưu lịch sử)
      │
      ▼ (Prisma Client & Redis Client)
[PostgreSQL & Redis Leaderboard]
```

### A. Tĩnh Tọa và Đồng bộ Thọ Nguyên (Offline Progress)
Khi người chơi ngắt kết nối (offline), backend chạy cron job định kỳ tính toán:
1. Tự động tăng tuổi thọ nhân vật (1 giờ ngoài đời = 1 năm trong game).
2. Tích lũy tu vi tĩnh tọa tự động (tối đa 8 giờ) dựa trên cấp độ Tụ Linh Trận và Linh Mạch chiếm giữ trong bảng `ActiveLinhMach`.
3. Nếu nhân vật vượt quá `maxAge` (thọ nguyên) mà chưa kịp đột phá, backend tự động chuyển trạng thái nhân vật sang **Luân Hồi** và lưu điểm Chân Linh. Khi người chơi đăng nhập lại, socket gửi gói tin `BreakthroughResponse` với cờ `reincarnated = true` để hướng dẫn người chơi khởi tạo nhân vật kiếp sau.

### B. Tranh Đoạt Linh Mạch (PVP)
1. Người chơi gửi yêu cầu chiếm giữ một mỏ linh mạch qua socket.
2. Backend kiểm tra số lượng mỏ hiện có trong bảng `ActiveLinhMach`.
3. Nếu mỏ đã có người chiếm giữ, hệ thống kích hoạt trận đấu PK tự động giữa hai người chơi dựa trên các chỉ số cảnh giới và pháp bảo lưu trong PostgreSQL.
4. Người chiến thắng được ghi nhận chiếm mỏ trong tối đa 4 giờ, tốc độ tăng tu vi trong Redis được cập nhật tương ứng.

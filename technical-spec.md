# ĐẶC TẢ KỸ THUẬT HỆ THỐNG: PORTRAIT XIANXIA WEB GAME

Tài liệu này đặc tả chi tiết kiến trúc kỹ thuật của dự án **Phàm Nhân**, bao gồm cấu trúc mã nguồn Frontend (React) và Backend (Express + Prisma), giao thức truyền tin nhị phân qua WebSocket bằng Protocol Buffers (Protobuf) và cấu hình ảo hóa Docker Production.

---

## 1. KIẾN TRÚC FRONTEND (REACT.JS)

Frontend được thiết kế gọn nhẹ, tương thích cao với thiết bị di động (Mobile Web), quản lý kết nối socket thời gian thực và tự động mã hóa/giải mã các gói tin nhị phân.

### 1.1. Cấu trúc thư mục đề xuất (React/Vite)
```
frontend/
├── public/
│   └── proto/
│       └── game.proto          # File định nghĩa Schema Protobuf dùng chung
├── src/
│   ├── assets/                 # Hình ảnh, icon vector tối giản (xianxia style)
│   ├── components/             # Các UI components tái sử dụng
│   │   ├── BottomNav.jsx       # Thanh điều hướng dọc (5 tab)
│   │   ├── CharacterHeader.jsx # Header thông tin nhân vật, thọ nguyên, tu vi
│   │   └── GlassModal.jsx      # Modal kính mờ Glassmorphism
│   ├── hooks/
│   │   └── useWebSocket.js     # Hook tùy chỉnh xử lý kết nối, gửi/nhận binary
│   ├── services/
│   │   └── protoService.js     # Trình quản lý load file .proto và encode/decode
│   ├── store/
│   │   └── gameStore.js        # Quản lý trạng thái Client (Zustand hoặc React Context)
│   ├── views/                  # Các view màn hình tương ứng với 5 tab
│   │   ├── CultivateView.jsx   # Tab Tu Luyện & Bát Quái
│   │   ├── AbodeView.jsx       # Tab Động Phủ (Linh điền, mỏ khoáng)
│   │   ├── WorldView.jsx       # Tab Giang Hồ (Kỳ ngộ, bí cảnh)
│   │   ├── InventoryView.jsx   # Tab Túi Đồ
│   │   └── RankingsView.jsx    # Tab Bảng Xếp Hạng
│   ├── App.jsx                 # Entrypoint chính của React
│   ├── index.css               # Chứa Design System tokens (glassmorphism, dark theme)
│   └── main.jsx
├── Dockerfile                  # Dockerfile build static site & chạy bằng Nginx
├── package.json
└── vite.config.js
```

### 1.2. Luồng Xử Lý Gói Tin Nhị Phân tại Frontend
1. **Khởi tạo kết nối**: Hook `useWebSocket.js` mở kết nối WebSocket đến Backend kèm JWT token tại query string (`ws://api.phamnhan.com?token=JWT_TOKEN`). Thiết lập `ws.binaryType = "arraybuffer"`.
2. **Gửi tin nhắn (Encode)**:
   - Client gọi hàm gửi: `sendAction(OPCODE, JSON_PAYLOAD)`.
   - `protoService.js` sử dụng đối tượng Protobuf tương ứng với OPCODE để mã hóa payload thành `Uint8Array`.
   - Tạo ra một `ArrayBuffer` mới: 2 bytes đầu tiên chứa OPCODE (số nguyên 16-bit), các bytes tiếp theo chứa dữ liệu đã mã hóa.
   - Gửi `ArrayBuffer` này qua socket.
3. **Nhận tin nhắn (Decode)**:
   - Khi sự kiện `onmessage` của WebSocket kích hoạt với dữ liệu là một `ArrayBuffer`.
   - Đọc 2 bytes đầu tiên bằng `DataView` để xác định OPCODE nhận được.
   - Cắt (slice) phần byte còn lại và chuyển qua `protoService.js` sử dụng đối tượng Protobuf tương ứng để giải mã (decode) thành đối tượng JSON gốc.
   - Cập nhật dữ liệu vào `gameStore.js` để re-render giao diện React.

---

## 2. KIẾN TRÚC BACKEND (EXPRESS + PRISMA + WEBSOCKET)

Backend quản lý logic game, xử lý các tác vụ tính toán thời gian thực (hấp thu linh khí, đếm ngược thọ nguyên) và tương tác trực tiếp với Database thông qua Prisma.

### 2.1. Cấu trúc thư mục đề xuất (Node.js/Express)
```
backend/
├── prisma/
│   ├── schema.prisma           # Định nghĩa Schema PostgreSQL
│   └── migrations/             # Lịch sử Database migration
├── src/
│   ├── config/
│   │   ├── database.js         # Khởi tạo Prisma Client
│   │   └── redis.js            # Kết nối Redis
│   ├── constants/
│   │   ├── opcodes.js          # Định nghĩa danh sách mã tin nhắn (OPCODE)
│   │   └── gameRules.js        # Hằng số thọ nguyên, tỷ lệ rơi, cấp độ lôi kiếp
│   ├── handlers/               # Xử lý các tin nhắn nhị phân nhận được qua socket
│   │   ├── authHandler.js
│   │   ├── cultivationHandler.js
│   │   ├── abodeHandler.js
│   │   ├── encounterHandler.js
│   │   └── pvpHandler.js
│   ├── middleware/
│   │   └── socketAuth.js       # Xác thực người chơi trước khi thiết lập kết nối socket
│   ├── proto/
│   │   └── game.proto          # File định nghĩa Schema Protobuf (đồng bộ với FE)
│   ├── services/
│   │   ├── protoService.js     # Đọc và biên dịch schema protobuf ở backend
│   │   ├── leaderboardService.js # Tương tác Redis Sorted Set
│   │   └── cronService.js      # Cron job phát thưởng tuần, trừ thọ nguyên tự động
│   ├── app.js                  # Entrypoint: Khởi tạo HTTP Express + WebSocket Server
│   └── socketRouter.js         # Phân phối tin nhắn socket nhị phân đến các handler
├── Dockerfile                  # Multi-stage Dockerfile cho backend
├── docker-compose.yml          # Docker Compose kết hợp toàn bộ dịch vụ
└── package.json
```

### 2.2. Luồng Định Tuyến Tin Nhắn Socket (Socket Router)
Thay vì sử dụng HTTP API truyền thống, toàn bộ chức năng game đều sử dụng WebSockets. Server sẽ lắng nghe sự kiện `connection`, kiểm tra xác thực và định tuyến các gói tin nhị phân:

```
[Client ArrayBuffer] 
         │
         ▼ (WebSocket Connection)
[WebSocket Server (ws)] ──► (Xác thực JWT Token) ──► Từ chối nếu sai
         │
         ▼ (Sự kiện "message")
[DataView: Read 2-byte Opcode] 
         │
         ├─► Opcode 1001 ──► [cultivationHandler.js] ──► Bắt đầu Tĩnh tọa
         ├─► Opcode 1002 ──► [cultivationHandler.js] ──► Thực hiện Đột phá Lôi kiếp
         ├─► Opcode 2001 ──► [abodeHandler.js]       ──► Thu hoạch Linh Điền
         └─► Opcode 3001 ──► [encounterHandler.js]   ──► Gửi sự kiện Kỳ Ngộ
```

---

## 3. ĐẶC TẢ GIAO THỨC NHỊ PHÂN (BINARY PROTOCOL SPEC)

Để đảm bảo tối ưu hóa đường truyền, toàn bộ dữ liệu giao tiếp Client-Server được bọc trong một cấu trúc nhị phân đơn giản kết hợp với **Google Protocol Buffers (Protobuf)**.

### 3.1. Cấu trúc Gói Tin Nhị Phân (Binary Packet Layout)
Mỗi gói tin gửi đi hoặc nhận về là một mảng byte (`ArrayBuffer`) có bố cục như sau:

```
┌──────────────────────────┬──────────────────────────────────────────┐
│  OPCODE (2 Bytes)        │  PROTOBUF PAYLOAD (N Bytes)               │
│  Số nguyên 16-bit (uint16)│  Dữ liệu đã được serialize bằng Protobuf   │
└──────────────────────────┴──────────────────────────────────────────┘
```

* **Header (2 Bytes)**: Chứa giá trị Opcode để chỉ định hành động.
* **Payload (N Bytes)**: Nội dung chi tiết của dữ liệu. Nếu không có dữ liệu (ví dụ: yêu cầu Ping), Payload có kích thước bằng 0.

### 3.2. File Schema Protobuf: `game.proto`
Dưới đây là định nghĩa file `game.proto` dùng chung cho cả Frontend và Backend để đảm bảo tính đồng bộ dữ liệu:

```protobuf
syntax = "proto3";

package phamnhan;

// --- OPCODE 1000 - HỆ THỐNG & NHÂN VẬT ---

// Client kết nối hoặc yêu cầu cập nhật thông tin
message PlayerStatusRequest {}

// Server phản hồi thông tin trạng thái nhân vật
message PlayerStatusResponse {
  string username = 1;
  string realm = 2;              // Cảnh giới (ví dụ: Luyện Khí Tầng 1)
  int64 tu_vi = 3;               // Điểm tu vi hiện tại
  int64 required_tu_vi = 4;      // Điểm tu vi cần để đột phá
  int32 age = 5;                 // Tuổi hiện tại
  int32 max_age = 6;             // Giới hạn thọ nguyên
  int64 spirit_stones = 7;       // Linh thạch sở hữu
  int32 cultivation_speed = 8;   // Linh khí hấp thu mỗi giây
  int32 lineage_points = 9;      // Điểm chân linh luân hồi tích lũy
}

// --- OPCODE 1001 - TĨNH TỌA TU LUYỆN ---
message ToggleCultivateRequest {
  bool active = 1;               // true: Bắt đầu tĩnh tọa, false: Ngừng tĩnh tọa
}

message ToggleCultivateResponse {
  bool active = 1;
  int32 current_speed = 2;       // Tốc độ hấp thu thực tế sau khi tính toán các buff
}

// --- OPCODE 1002 - ĐỘT PHÁ & THIÊN KIẾP ---
message BreakthroughRequest {
  repeated string use_item_ids = 1; // Danh sách ID đan dược/pháp bảo sử dụng để tăng tỷ lệ (ví dụ: ["item_truc_co_dan"])
}

message BreakthroughResponse {
  bool success = 1;              // Kết quả đột phá
  string new_realm = 2;          // Cảnh giới mới (nếu thành công)
  string message = 3;            // Thông điệp kết quả (ví dụ: "Đột phá thành công", "Thất bại bị trọng thương", "Tử vong đi vào Luân hồi")
  int64 tu_vi_lost = 4;          // Điểm tu vi bị tổn hao nếu thất bại
  bool reincarnated = 5;         // Nhân vật có bị luân hồi hay không
}

// --- HỆ THỐNG ĐỘNG PHỦ PHÂN TẦNG ---

// OPCODE 2000 - Xem danh sách 100 ô đất của một tầng
message GetAbodeFloorRequest {
  int32 floor = 1;
}

message AbodePlotInfo {
  int32 plot_index = 1;          // Số thứ tự ô từ 1 đến 100
  string owner_id = 2;           // UUID người đang sở hữu, rỗng nếu chưa có ai mua
  string owner_name = 3;         // Tên người sở hữu
}

message GetAbodeFloorResponse {
  int32 floor = 1;
  repeated AbodePlotInfo plots = 2; // Danh sách 100 ô của tầng đó
}

// OPCODE 2001 - Mua ô đất động phủ
message BuyAbodePlotRequest {
  int32 floor = 1;
  int32 plot_index = 2;          // Số thứ tự ô muốn mua (1 -> 100)
}

message BuyAbodePlotResponse {
  bool success = 1;
  string message = 2;            // Kết quả (ví dụ: "Mua thành công", "Ô đã bị người khác mua")
  int32 purchased_floor = 3;
  int32 purchased_plot_index = 4;
  int64 spirit_stones_spent = 5; // Số linh thạch đã tiêu tốn
}

// OPCODE 2002 - Di chuyển lên tầng trên
message MoveUpFloorRequest {}

message MoveUpFloorResponse {
  bool success = 1;
  string message = 2;
  int32 new_floor = 3;
  int32 new_plot_index = 4;      // Ô đất ngẫu nhiên hoặc được chọn tự động ở tầng mới
  int64 refund_stones = 5;       // Linh thạch được hoàn trả 50% từ ô đất cũ
}

// OPCODE 2003 - Thu hoạch Linh Điền
message HarvestLinhDienRequest {
  int32 field_index = 1;         // Ô đất trồng cần thu hoạch (0 -> 5)
}

message HarvestLinhDienResponse {
  bool success = 1;
  string item_id = 2;            // Vật phẩm thu hoạch được
  int32 quantity = 3;            // Số lượng thu hoạch
}

// OPCODE 2004 - Cho thú ăn ở Yêu Vực
message FeedBeastRequest {
  int32 beast_cage_index = 1;    // Ô chuồng nuôi (0 -> 2)
  string food_item_id = 2;       // ID vật phẩm làm thức ăn
  int32 quantity = 3;
}

message FeedBeastResponse {
  bool success = 1;
  string message = 2;
  int32 new_growth_percentage = 3; // Độ trưởng thành mới của thú
}

// --- OPCODE 3001 - GIANG HỒ KỲ NGỘ ---
message TravelRequest {}

message TravelResponse {
  string title = 1;              // Tiêu đề kỳ ngộ
  string description = 2;        // Nội dung mô tả kỳ ngộ
  repeated string options = 3;    // Danh sách các lựa chọn tình huống (Tối đa 3)
}

message ChooseOptionRequest {
  int32 option_index = 1;        // Lựa chọn của người chơi (0, 1, 2)
}

message ChooseOptionResponse {
  bool success = 1;
  string result_description = 2; // Kết quả của lựa chọn
  int64 tu_vi_reward = 3;        // Tu vi nhận/mất
  int64 spirit_stones_reward = 4;// Linh thạch nhận/mất
  string item_reward_id = 5;     // Vật phẩm nhận được
}
```

---

## 4. CẤU HÌNH DOCKER & PRODUCTION ORCHESTRATION

Toàn bộ hệ thống được container hóa sử dụng Docker để dễ dàng triển khai trên VPS hoặc Cloud Server.

### 4.1. Dockerfile cho Backend (`backend/Dockerfile`)
Dockerfile cho Backend sử dụng multi-stage build để giảm thiểu kích thước image cuối cùng, chỉ giữ lại code đã build và dependencies cần thiết.

```dockerfile
# --- Stage 1: Build & Install Dependencies ---
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
COPY prisma ./prisma/

# Cài đặt tất cả dependencies bao gồm cả devDependencies để build
RUN npm ci

COPY . .

# Generate Prisma Client
RUN npx prisma generate

# --- Stage 2: Runner ---
FROM node:18-alpine AS runner

WORKDIR /app

ENV NODE_ENV=production

COPY package*.json ./

# Chỉ cài đặt production dependencies
RUN npm ci --only=production

# Copy built artifacts từ builder
COPY --from=builder /app/node_modules/.prisma ./node_modules/.prisma
COPY --from=builder /app/node_modules/@prisma/client ./node_modules/@prisma/client
COPY --from=builder /app/prisma ./prisma
COPY --from=builder /app/src ./src

EXPOSE 4000

# Khởi chạy server: chạy db migration và start node server
CMD ["sh", "-c", "npx prisma migrate deploy && node src/app.js"]
```

### 4.2. Dockerfile cho Frontend (`frontend/Dockerfile`)
Frontend React được build tĩnh và phân phối thông qua máy chủ Web Nginx hiệu năng cao.

```dockerfile
# --- Stage 1: Build React App ---
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# --- Stage 2: Serve with Nginx ---
FROM nginx:alpine

# Copy built files từ builder sang thư mục phục vụ của nginx
COPY --from=builder /app/dist /usr/share/nginx/html

# Cấu hình Nginx tùy chỉnh để hỗ trợ Single Page Application (SPA routing)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

#### Nginx Configuration (`frontend/nginx.conf`)
```nginx
server {
    listen 80;
    server_name localhost;

    location / {
        root /usr/share/nginx/html;
        index index.html index.htm;
        try_files $uri $uri/ /index.html;
    }

    # Hỗ trợ reverse proxy cho kết nối websocket nếu cần chung port
    location /ws {
        proxy_pass http://backend:4000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_set_header Host $host;
    }
}
```

### 4.3. Docker Compose Orchestration (`docker-compose.yml`)
Tệp docker-compose liên kết tất cả các container cần thiết thành một hệ thống đồng nhất.

```yaml
version: '3.8'

services:
  # --- Database ---
  postgres:
    image: postgres:15-alpine
    container_name: phamnhan_postgres
    restart: always
    environment:
      POSTGRES_USER: phamnhan_user
      POSTGRES_PASSWORD: StrongPassword123
      POSTGRES_DB: phamnhan_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  # --- Cache & Leaderboard ---
  redis:
    image: redis:7-alpine
    container_name: phamnhan_redis
    restart: always
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  # --- Backend Server ---
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: phamnhan_backend
    restart: always
    environment:
      DATABASE_URL: "postgresql://phamnhan_user:StrongPassword123@postgres:5432/phamnhan_db?schema=public"
      REDIS_URL: "redis://redis:6379"
      JWT_SECRET: "SecretXianxia2026"
      PORT: 4000
    ports:
      - "4000:4000"
    depends_on:
      - postgres
      - redis

  # --- Frontend Client ---
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: phamnhan_frontend
    restart: always
    ports:
      - "80:80"
    depends_on:
      - backend

volumes:
  postgres_data:
  redis_data:
```

# NHIỆM VỤ HIỆN TẠI (CURRENT TASK & PROGRESS)

Hệ thống game server và client **Phàm Nhân Tu Tiên: Mạt Pháp Chi Lộ** đã được lập trình hoàn thành 100%, tích hợp kiểm tra cục bộ biên dịch thành công.

---

## 1. MỤC TIÊU HIỆN TẠI (CURRENT FOCUS)
* Nghiệm thu mã nguồn Backend Node.js và Frontend React.
* Hướng dẫn chạy thử bằng Docker Compose và kiểm tra hệ thống socket nhị phân qua Protobuf.

---

## 2. DANH SÁCH CÔNG VIỆC (TODO LIST)

### A. Thiết lập Quy tắc AI (Hoàn thành)
- [x] Tạo `GEMINI.md` làm rule chính cho Antigravity.
- [x] Tạo `AGENTS.md` làm rule dùng chung cho các AI khác.
- [x] Khởi tạo các tài liệu Memory Bank (`project.md`, `architecture.md`, `coding-style.md`, `api.md`, `database.md`, `mistakes.md`, `decisions.md`).

### B. Khởi tạo dự án FE & BE (Hoàn thành)
- [x] Khởi tạo dự án Backend Express và Frontend React (Vite).
- [x] Thiết lập Prisma Schema và chạy migrations đầu tiên với PostgreSQL.
- [x] Viết cấu hình Dockerfile cho cả backend và frontend.
- [x] Tạo file docker-compose.yml và cấu hình môi trường (.env.example).

### C. Logic Game & Socket Binary (Hoàn thành)
- [x] Tạo file protobuf định nghĩa `game.proto` đồng bộ cho cả FE và BE.
- [x] Xây dựng WebSocket Server tích hợp xử lý parse Opcode + decode Protobuf nhị phân ở Backend.
- [x] Xây dựng module kết nối WebSocket, encode/decode nhị phân ở React Frontend.
- [x] Viết các handlers ở Backend: Cultivation (Tĩnh tọa, Đột phá lôi kiếp), Abode (Linh điền), Encounter (Kỳ ngộ), PVP (Chiếm mỏ).
- [x] Xây dựng Redis Leaderboard Service để xếp hạng thời gian thực.
- [x] Thiết lập cron job chạy ngầm tính offline progress, thọ nguyên và phát thưởng tuần.

### D. Thiết Kế Game (Hoàn thành)
- [x] Tạo file thiết kế chi tiết game [game-design.md](file:///c:/Users/phong/OneDrive/Desktop/inputdata/tucode/phamnhan/game-design.md) tại thư mục gốc.
- [x] Tạo file đặc tả kỹ thuật chi tiết [technical-spec.md](file:///c:/Users/phong/OneDrive/Desktop/inputdata/tucode/phamnhan/technical-spec.md) tại thư mục gốc.
- [x] Tạo thư mục [game-rules/](file:///c:/Users/phong/OneDrive/Desktop/inputdata/tucode/phamnhan/game-rules/) lưu trữ các tính năng và quy tắc chi tiết.

---

## 3. THÔNG TIN PHIÊN LÀM VIỆC (SESSION LOGS)
* **2026-06-15**: Thiết lập toàn bộ cấu trúc mã nguồn trong `backend/` và `frontend/`.
* **2026-06-15**: Viết schema Prisma PostgreSQL, định cấu hình Protobuf nhị phân ở cả server và client.
* **2026-06-15**: Lập trình hoàn tất toàn bộ logic Tu luyện, Thọ Nguyên lão hoá, Đột phá lôi kiếp nguy hiểm, Luân hồi thừa kế linh căn.
* **2026-06-15**: Hoàn tất xây dựng Thông thiên tháp căn hộ xã hội, 6 ô linh điền trồng trọt, 3 chuồng yêu thú nuôi dưỡng.
* **2026-06-15**: Xây dựng kịch bản Kỳ ngộ du ngoạn ngẫu nhiên, tranh đoạt mỏ linh mạch PVP tính toán lực chiến CP tự động.
* **2026-06-15**: Đóng gói Docker Compose, chạy biên dịch dev build thành công rực rỡ.
* **2026-06-15**: Tích hợp và cấu hình hệ thống Tailwind CSS v4 chuẩn cho Vite React sử dụng `@tailwindcss/vite` để giải quyết triệt để lỗi mất định dạng giao diện.
* **2026-06-15**: Cải tiến giao diện màn hình Đăng Nhập & Chọn Linh Căn theo quy chuẩn tiên hiệp cổ điển, đồng bộ padding 16px (p-4), căn chỉnh icon chuẩn xác và thêm hiệu ứng động mượt mà.
* **2026-06-15**: Giải quyết sự cố Backend không thể hoạt động do thiếu database `phamnhan_db` trên MySQL; đồng bộ schema qua `npx prisma db push`, khởi chạy thành công BE trên cổng 1113 và kiểm thử E2E đăng ký trơn tru.
* **2026-06-15**: Cập nhật tài liệu thiết kế giao diện frontend-rules.md trong Memory Bank. Khắc phục triệt để lỗi chồng chéo icon nhập liệu trên input bằng CSS padding cố định 2.75rem. Nâng cấp toàn diện giao diện (Auth, Chọn Linh Căn, Bát Quái Tu luyện, Linh điền Động phủ, Yêu Vực, BXH, Hòm đồ phẩm cấp) sang chủ đề Cyber-Xianxia bọc trong khung điện thoại Obsidian sang trọng cho Desktop. Loại bỏ trường nhập Email ở cả Backend & Frontend trong quá trình đăng ký tài khoản.
* **2026-06-16**: Tích hợp log chi tiết socket (inbound và outbound) khi chạy ở chế độ dev để dễ dàng debug các gói tin nhị phân.
* **2026-06-16**: Sửa lỗi không chuyển màn hình chính sau khi chọn đạo lộ bằng cách cấu hình `keepCase: true` cho `protobuf.load` ở cả Frontend & Backend. Đồng thời đồng bộ file `game.proto` của Frontend, tích hợp trường `abode_plot` vào `PlayerStatusResponse` ở backend, và cập nhật component `AbodeView` sang chuẩn snake_case đồng bộ.
* **2026-06-16**: Cập nhật [game-design.md](file:///c:/Users/phong/OneDrive/Desktop/inputdata/tucode/phamnhan/game-design.md) với plan UI Frontend chi tiết cho MVP: AppShell portrait, component cốt lõi, design tokens, từng màn hình chính, state/socket UX, responsive/accessibility và checklist build theo giai đoạn.
* **2026-06-16**: Cập nhật rule dành cho AI khi code Frontend trong [AGENTS.md](file:///c:/Users/phong/OneDrive/Desktop/inputdata/tucode/phamnhan/AGENTS.md) và [memory-bank/frontend-rules.md](file:///c:/Users/phong/OneDrive/Desktop/inputdata/tucode/phamnhan/memory-bank/frontend-rules.md), gồm nguồn tham chiếu bắt buộc, AppShell portrait, component core loop, Zustand/socket state, Tailwind visual rules, loading/error states và các điều không được làm.
* Người thực hiện: Antigravity AI.

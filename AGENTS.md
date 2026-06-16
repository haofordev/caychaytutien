# HƯỚNG DẪN DÙNG CHUNG CHO CÁC AI AGENTS (AGENTS.md)
*(Áp dụng cho Cursor, Claude, ChatGPT, GitHub Copilot, v.v.)*

Chào AI Agent, bạn đang làm việc trên dự án này cùng với nhà phát triển. Để duy trì tính ổn định, dễ bảo trì và tránh xung đột code, bạn bắt buộc phải tuân theo các hướng dẫn sau:

---

## 1. KHÔNG LÀM MẤT KHÔNG GIAN BỘ NHỚ (MEMORY BANK)
Dự án sử dụng hệ thống **Memory Bank** nằm trong thư mục `memory-bank/` làm nguồn chân lý (Source of Truth) cho trạng thái dự án.
- **Trước khi làm bất cứ việc gì**: Hãy đọc các file trong `memory-bank/` để hiểu kiến trúc (`architecture.md`), phong cách code (`coding-style.md`), và nhiệm vụ hiện tại (`current-task.md`).
- **Sau khi hoàn thành task**: Cập nhật tiến độ của bạn vào `memory-bank/current-task.md` và ghi lại bất kỳ quyết định kỹ thuật quan trọng nào vào `memory-bank/decisions.md`.
- **Nếu gặp bug**: Sau khi sửa xong, hãy note lại nguyên nhân và giải pháp vào `memory-bank/mistakes.md` để các AI khác không lặp lại lỗi này.

---

## 2. QUY TẮC PHÁT TRIỂN & VIẾT CODE
- **Viết Code Sạch (Clean Code)**: Ưu tiên sự rõ ràng hơn là ngắn gọn. Viết code tự giải thích (self-documenting code), đặt tên biến/hàm mang tính mô tả rõ nghĩa.
- **Tuân thủ Coding Style**: Đọc kỹ `memory-bank/coding-style.md` trước khi code. Không tự ý viết theo thói quen riêng của bạn nếu nó đi ngược lại quy tắc chung của dự án.
- **Không Xoá Chú Thích (Comments)**: Giữ nguyên các dòng comment, JSDoc hoặc docstring cũ không liên quan trực tiếp đến sửa đổi của bạn. Hãy bổ sung comment cho các đoạn logic phức tạp mới.
- **Không tự ý cài đặt Packages**: Không tự động cài đặt các thư viện mới (`npm install`, `pip install`, v.v.) trừ khi được người dùng yêu cầu rõ ràng. Hãy đề xuất trước khi cài đặt.

---

## 3. QUY TẮC GIT COMMITS
Khi thực hiện commit hoặc tạo mô tả cho pull request, hãy sử dụng chuẩn **Conventional Commits**:
- `feat`: Tính năng mới
- `fix`: Sửa lỗi
- `docs`: Thay đổi tài liệu
- `style`: Thay đổi định dạng code (formatting, semicolon, v.v. - không ảnh hưởng logic)
- `refactor`: Tái cấu trúc code (không sửa lỗi cũng không thêm tính năng)
- `test`: Thêm hoặc sửa test cases
- `chore`: Cập nhật build tasks, package manager, v.v.

Ví dụ: `feat(auth): add google login integration`

---

## 4. TƯƠNG TÁC VỚI NGƯỜI DÙNG
- Giữ phản hồi ngắn gọn, đi thẳng vào vấn đề.
- Trình bày mã nguồn rõ ràng trong các block code markdown kèm theo ngôn ngữ lập trình cụ thể.
- Đưa ra giải pháp tối ưu kèm theo phân tích ngắn gọn lý do tại sao chọn giải pháp đó.

---

## 5. QUY TẮC BẮT BUỘC KHI CODE FRONTEND
Khi được yêu cầu xây dựng, sửa hoặc refactor giao diện Frontend, AI Agent bắt buộc tuân theo các rule sau:

### 5.1. Đọc tài liệu trước khi code
Trước khi sửa FE, hãy đọc tối thiểu các file sau:
- `memory-bank/frontend-rules.md`: source of truth cho UI/UX, theme, layout, interaction.
- `game-design.md` mục **6. Thiết Kế Giao Diện Màn Hình Dọc**: source of truth cho AppShell portrait, component tree, states và checklist build FE.
- `memory-bank/architecture.md`: kiểm tra flow React/Zustand/WebSocket/Protobuf.
- Các component/store hiện có trong `frontend/src/` liên quan trực tiếp đến task.

### 5.2. Nguyên tắc thiết kế Mobile-first
- Không tạo landing page/marketing page nếu người dùng yêu cầu build game UI. Màn hình đầu tiên sau đăng nhập phải là giao diện chơi thật.
- Giữ layout portrait, mobile-first, chiều rộng game tối đa `450px`, desktop hiển thị trong khung thiết bị/phone frame.
- Không để header, event log hoặc bottom nav chiếm quá nhiều chiều cao khiến vùng chơi chính bị chật trên mobile nhỏ.
- Mọi control có tương tác phải có hit target tối thiểu `44px`.
- Text dài phải xuống dòng hợp lý hoặc đưa vào modal/bottom sheet, không để tràn hoặc chồng lên UI khác.

### 5.3. Nguyên tắc visual Cyber-Xianxia
- Dùng Dark Mode + Glassmorphism làm nền tảng: panel mờ, blur nhẹ, border mảnh, glow tiết chế.
- Giữ cảm giác Mạt Pháp u tối, cạn kiệt linh khí; chỉ dùng neon accent làm điểm nhấn.
- Màu hệ tu phải nhất quán:
  - Đạo Tu: emerald/jade.
  - Thể Tu: orange/fire.
  - Ma Tu: fuchsia/toxic purple.
  - Linh thạch/CTA chính: amber/gold.
- Không biến toàn bộ giao diện thành một màu tím/xanh/vàng đơn điệu. Màu accent chỉ dùng cho trạng thái, phẩm cấp, CTA và feedback.

### 5.4. Component và state
- Ưu tiên dùng AppShell portrait gồm: `PlayerStatusHeader`, `CultivationProgress`, `MainViewport`, `EventLogDrawer`, `BottomNavigation`.
- Tách UI thành component nhỏ, tên rõ nghĩa, dùng `PascalCase` cho component và `camelCase` cho props/state.
- State FE phải tách theo domain bằng Zustand hoặc pattern hiện có: auth, player, cultivation, abode, world, inventory, ranking, event log, socket.
- Không hardcode dữ liệu gameplay lâu dài trong component. Dữ liệu cấu hình phải nằm trong constants/config hoặc nhận từ socket/store.
- Mỗi action gửi socket phải có trạng thái `pending`, `success`, `error` và khóa nút liên quan để tránh spam request.

### 5.5. WebSocket, Protobuf và dữ liệu
- Không đổi schema Protobuf, opcode hoặc format payload nếu task không yêu cầu rõ.
- Tôn trọng quy ước `keepCase: true` và dữ liệu snake_case đã đồng bộ giữa FE/BE.
- Khi mất kết nối socket, UI vẫn đọc được dữ liệu cache nhưng khóa các action ghi dữ liệu.
- Khi reconnect, cần đồng bộ lại trạng thái nhân vật, túi đồ, động phủ và log sự kiện nếu task chạm đến các vùng này.

### 5.6. Loading, error và micro-interactions
- Mỗi màn hình có dữ liệu async phải có skeleton loading giữ nguyên kích thước layout để tránh layout shift.
- Button phải có đủ states: `default`, `hover`, `active`, `disabled`, `loading`, `success`, `error`.
- Feedback gameplay phải ghi vào event log ngắn gọn: nhận thưởng, thất bại, trọng thương, đột phá, thu hoạch, mất kết nối.
- Animation phải nhẹ, không gây giảm hiệu năng; hỗ trợ `prefers-reduced-motion` khi thêm animation lớn.

### 5.7. Giới hạn thay đổi
- Không tự ý cài package UI/icon/animation mới. Nếu thật sự cần, hãy đề xuất trước.
- Không refactor toàn bộ FE khi task chỉ yêu cầu một màn hình/component.
- Không xóa comment, JSDoc, class hoặc helper cũ nếu không liên quan trực tiếp.
- Sau khi hoàn thành, cập nhật `memory-bank/current-task.md`; nếu có quyết định FE quan trọng, ghi thêm vào `memory-bank/decisions.md`.

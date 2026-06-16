# QUY TẮC PHÁT TRIỂN GIAO DIỆN (FRONTEND DESIGN & CODE RULES)

Tài liệu này quy định các tiêu chuẩn thiết kế giao diện (UI) và trải nghiệm người dùng (UX) cho dự án **Phàm Nhân Tu Tiên: Mạt Pháp Chi Lộ**. Giao diện phải mang đậm phong cách tiên hiệp cổ điển kết hợp phong cách hiện đại (Modern Oriental / Cyber-Xianxia Vibe), mang lại cảm giác huyền bí, cao cấp và mượt mà.

---

## 1. HỆ THỐNG MÀU SẮC (THEME & COLOR PALETTE)

Tránh sử dụng các màu đơn sắc thô (generic colors). Sử dụng các dải màu chuyển (gradients) và độ mờ để tạo chiều sâu huyền ảo của thế giới tu chân:

| Thành phần | Mã màu / Gradient đề xuất | Mô tả ý nghĩa |
| :--- | :--- | :--- |
| **Nền chính (Background)** | `radial-gradient(circle at top, #0f172a 0%, #020617 100%)` | Đêm tối vô tận, linh khí mờ ảo |
| **Thẻ chứa (Card / Panel)** | `rgba(15, 23, 42, 0.65)` với blur `16px` và border `rgba(255, 255, 255, 0.05)` | Glassmorphism huyền ảo, tinh khiết |
| **Tông màu Vàng Kim** | `#f59e0b` (Amber) -> `#d97706` (Gold) | Linh thạch, tôn quý, hoàng gia, đột phá thành công |
| **Tông màu Đạo Tu** | `#10b981` (Emerald) -> `#059669` (Jade) | Linh thảo, mộc hệ linh căn, chính đạo thanh khiết |
| **Tông màu Thể Tu** | `#f97316` (Orange) -> `#ea580c` (Fire) | Nhục thân rèn luyện, lôi kiếp hoả thiêu |
| **Tông màu Ma Tu** | `#d946ef` (Fuchsia) -> `#c084fc` (Purple) | Sát phạt chứng đạo, tà ma chi khí |
| **Đường viền phát sáng** | `rgba(245, 158, 11, 0.15)` | Hào quang linh khí xung quanh vật phẩm / khung |

---

## 2. KIỂU CHỮ (TYPOGRAPHY)

* **Font chữ tiêu đề (Headings)**: Sử dụng font `Outfit` hoặc `Playfair Display`. Cỡ chữ lớn, có thể kèm theo dải gradient vàng kim hoặc bạc để làm nổi bật tên cảnh giới/vật phẩm.
* **Font chữ nội dung (Body)**: Sử dụng font `Inter` hoặc `Segoe UI` để đảm bảo độ đọc tốt nhất ở kích thước nhỏ trên thiết bị di động.
* **Độ tương phản**: Đảm bảo phân cấp chữ rõ ràng (Hierarchy). Chữ nhãn (labels) sử dụng chữ in hoa nhỏ (`uppercase tracking-wider text-[10px] text-slate-400`).

---

## 3. CHỐNG LỖI CHỒNG CHÉO & THIẾT KẾ INPUTS (INPUT INTERFACE SAFETY)

Để ngăn ngừa triệt để lỗi biểu tượng (icon) đè lên nội dung placeholder/chữ nhập liệu:
* **Quy tắc gói (Wrapper)**: Mọi ô nhập liệu có icon đều phải sử dụng thẻ bao bọc `relative flex items-center` hoặc class `.auth-input-wrapper`.
* **Icon căn giữa**: Icon bên trái phải được đặt tuyệt đối với `position: absolute`, `left` cố định (`left-3.5` hoặc `14px`), và căn giữa dọc thông qua `top-1/2 -translate-y-1/2`.
* **Padding an toàn**: Ô nhập liệu (`input`) bắt buộc phải có `padding-left` tối thiểu là `2.75rem` (`pl-11` hoặc `44px`) để tránh đè lên icon. Không sử dụng các giá trị padding-left nhỏ hơn đối với các ô chứa icon 16px.
* **Quy tắc Focus**: Khi focus, đường viền phải chuyển màu vàng kim mờ kèm hiệu ứng phát sáng nhẹ (`shadow-[0_0_12px_rgba(245,158,11,0.15)]` và `border-amber-500/40`).

---

## 4. NÚT NHẤN & HIỆU ỨNG TƯƠNG TÁC (BUTTONS & INTERACTION)

* **Nút chính (Primary)**: Sử dụng gradient vàng kim ấm áp (`bg-gradient-to-r from-amber-500 via-yellow-500 to-amber-600`).
* **Hiệu ứng Micro-animations**:
  * **Hover**: Nút hơi nổi lên nhẹ (`transform -translate-y-[1px]`), bóng đổ linh thạch tăng lên (`shadow-[0_4px_12px_rgba(245,158,11,0.3)]`).
  * **Active**: Nút hơi xẹp xuống khi nhấp (`active:scale-[0.97]`).
  * **Disabled**: Giảm độ mờ (`opacity-50`), loại bỏ mọi hiệu ứng hover/active và đặt con trỏ `cursor-not-allowed`.
* **Nút phụ / Nút chuyển chế độ (Secondary / Ghost)**: Sử dụng text màu vàng kim nhạt, hover có gạch chân nhẹ, hiệu ứng chuyển màu chữ mượt mà.

---

## 5. BỐ CỤC KHUNG THIẾT BỊ (PORTRAIT LAYOUT & OUTER FRAME)

* **Quy chuẩn hiển thị**: Game có chiều rộng tối đa là `450px`, căn giữa màn hình (`mx-auto`).
* **Khung Obsidian viền ngoài (Outer Device Frame)**: Khi hiển thị trên màn hình Desktop lớn, game phải được bao bọc trong một khung viền obsidian sang trọng (`.phone-frame-container`), giả lập màn hình dọc của một thiết bị di động cao cấp, ngăn cách màn hình game với nền tối bên ngoài của trình duyệt.
* **Bố cục nội dung**: Đảm bảo khoảng đệm (padding) tiêu chuẩn xung quanh là `16px` (`p-4`), tránh để chữ/nút chạm mép khung máy.

---

## 6. PHÂN LOẠI PHẨM CẤP VẬT PHẨM (ITEM QUALITY DESIGN SYSTEM)

Mọi vật phẩm trong túi đồ (Inventory) hoặc phần thưởng đều phải tuân theo màu sắc phân cấp phẩm vật để tạo động lực săn lùng:
* **Thường (Common - Trắng/Xám)**: Đường viền `border-slate-800`, màu nền dịu nhẹ.
* **Huyền Phẩm (Uncommon - Xanh Lục)**: Đường viền `border-emerald-500/20`, màu nền phát sáng nhẹ `bg-emerald-500/5`.
* **Linh Bảo (Rare - Xanh Lam)**: Đường viền `border-sky-500/20`, màu nền phát sáng nhẹ `bg-sky-500/5`.
* **Trân Phẩm (Epic - Tím)**: Đường viền `border-fuchsia-500/35`, màu nền phát sáng nhẹ `bg-fuchsia-500/5`.
* **Cực Phẩm (Legendary - Vàng Kim)**: Đường viền `border-amber-500/40`, màu nền phát sáng đặc biệt `bg-amber-500/10` kèm hiệu ứng shadow phát sáng vàng nhạt.

---

## 7. QUY TẮC CHO AI KHI TRIỂN KHAI FRONTEND (AI IMPLEMENTATION RULES)

Phần này là checklist bắt buộc dành cho Cursor, Claude, ChatGPT, Copilot hoặc bất kỳ AI Agent nào khi code giao diện Frontend của dự án.

### 7.1. Nguồn tham chiếu bắt buộc
Trước khi code, AI phải đọc và bám theo thứ tự ưu tiên:
1. `memory-bank/frontend-rules.md` - quy chuẩn UI/UX và visual system.
2. `game-design.md` mục **6. Thiết Kế Giao Diện Màn Hình Dọc** - AppShell, component tree, state, socket UX, checklist MVP.
3. `memory-bank/architecture.md` - kiến trúc React, Zustand, WebSocket, Protobuf.
4. Component/store hiện có trong `frontend/src/` - pattern thực tế của codebase.

Không tự tạo phong cách UI mới nếu mâu thuẫn với các tài liệu trên.

### 7.2. AppShell và bố cục màn hình
* Mọi màn gameplay phải nằm trong AppShell portrait, không build dạng dashboard desktop full-width.
* Chiều rộng nội dung game tối đa `450px`, desktop dùng phone frame để bọc UI.
* Header trạng thái, main viewport, event log và bottom navigation phải có kích thước ổn định, không gây layout shift khi dữ liệu thay đổi.
* `BottomNavigation` cố định đáy, `z-index` cao hơn nội dung cuộn; nội dung chính phải có padding-bottom đủ để không bị che.
* Không đặt card lồng trong card nếu chỉ để trang trí. Panel dùng để nhóm chức năng thật.

### 7.3. Component bắt buộc cho core loop
Khi task chạm tới gameplay chính, ưu tiên tái sử dụng hoặc tạo các component sau:
* `PlayerStatusHeader`: avatar, cảnh giới, linh căn, thọ nguyên, tài nguyên chính.
* `CultivationProgress`: thanh tu vi, `currentExp / requiredExp`, tốc độ linh khí/giây.
* `PrimaryActionButton`: CTA có icon, loading, disabled, success, error.
* `ResourcePill`: hiển thị linh thạch, linh dược, khoáng thạch, yêu đan, lượt du ngoạn.
* `EventLogDrawer`: log gameplay thu gọn/mở rộng.
* `ItemQualityFrame`: frame phẩm cấp vật phẩm theo màu quy định.
* `BottomSheet` hoặc `GameModal`: dùng cho chi tiết vật phẩm, xác nhận đột phá, chọn hỗ trợ lôi kiếp.

### 7.4. State và socket
* Dùng Zustand hoặc store pattern hiện có; không nhét toàn bộ state socket vào một component lớn.
* Tách state theo domain: auth, player, cultivation, abode, world, inventory, ranking, event log, socket.
* Mỗi socket action phải có local `requestId` hoặc pending key để chống spam click.
* Không optimistic update các tài nguyên quan trọng như tu vi, linh thạch, vật phẩm nếu backend chưa xác nhận.
* Khi socket error, giữ dữ liệu cũ, mở feedback ngắn và ghi log cảnh báo.
* Khi socket reconnect, cần request sync lại dữ liệu liên quan đến màn hiện tại.

### 7.5. Quy tắc visual khi code Tailwind
* Dùng `p-4` hoặc spacing tương đương `16px` cho padding màn hình.
* Panel glassmorphism dùng nền tối trong suốt, blur, border mảnh; không dùng shadow quá nặng.
* CTA chính dùng amber/gold; success dùng emerald; warning/lôi kiếp dùng orange/fire; ma khí/rare event dùng fuchsia/purple.
* Không dùng text hero quá lớn trong panel nhỏ. Heading trong card/panel phải gọn, dễ scan.
* Không dùng font-size theo viewport width. Dùng scale cố định và responsive bằng layout.
* Input có icon phải dùng wrapper `relative` và padding-left tối thiểu `2.75rem`.

### 7.6. Loading, disabled, error
Mọi component có dữ liệu async phải xử lý đủ trạng thái:
* **Default**: hiển thị dữ liệu thật từ store/socket.
* **Loading**: skeleton giữ nguyên kích thước vùng UI.
* **Disabled**: giảm opacity, khóa pointer, bỏ hover glow, ghi rõ lý do nếu là hành động quan trọng.
* **Success**: feedback ngắn bằng event log/toast, glow nhẹ một lần.
* **Error**: không làm mất dữ liệu cũ, hiển thị lỗi ngắn, cho phép retry nếu phù hợp.

### 7.7. Accessibility và mobile ergonomics
* Hit target tối thiểu `44px`.
* Nội dung quan trọng không được bị bottom nav hoặc safe-area che.
* Modal/bottom sheet phải đóng được bằng ESC trên desktop và nút đóng rõ trên mobile.
* Color không được là tín hiệu duy nhất; trạng thái quan trọng cần có text/icon đi kèm.
* Animation lớn phải tôn trọng `prefers-reduced-motion`.

### 7.8. Những điều không được làm
* Không tự cài package mới nếu chưa được người dùng đồng ý.
* Không đổi Protobuf schema/opcode khi task chỉ là UI.
* Không hardcode mock data vào production component.
* Không xóa comment/JSDoc/helper cũ không liên quan.
* Không refactor toàn bộ folder `frontend/` khi chỉ sửa một màn hình.
* Không tạo landing page, hero marketing hoặc layout desktop SaaS cho gameplay.

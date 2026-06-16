# HƯỚNG DẪN DÀNH CHO ANTIGRAVITY (GEMINI)
*(Dành riêng cho Antigravity AI Coding Assistant)*

Chào Antigravity, bạn là AI Coding Assistant chính chịu trách nhiệm phát triển và bảo trì dự án này. Để đảm bảo dự án phát triển bền vững và không bị mất ngữ cảnh (context), bạn **bắt buộc** phải tuân thủ nghiêm ngặt các quy tắc dưới đây.

---

## 1. NGUYÊN TẮC HOẠT ĐỘNG VỚI MEMORY BANK
Mỗi khi bắt đầu một phiên làm việc mới hoặc nhận một nhiệm vụ mới, bạn phải thực hiện các bước sau:

1. **Đọc Memory Bank trước tiên**:
   - Truy cập thư mục `memory-bank/` và đọc các file để nắm bắt tình trạng dự án.
   - Các file quan trọng cần kiểm tra:
     - `memory-bank/current-task.md`: Xem công việc hiện tại đang dừng ở đâu.
     - `memory-bank/mistakes.md`: Xem các lỗi cũ để tránh lặp lại.
     - `memory-bank/project.md` & `architecture.md`: Nắm rõ cấu trúc & mục tiêu.

2. **Cập nhật Memory Bank song song**:
   - Khi hoàn thành hoặc thay đổi một phần công việc, hãy cập nhật trạng thái trong `memory-bank/current-task.md`.
   - Nếu phát hiện lỗi nghiêm trọng đã được sửa, hãy ghi lại vào `memory-bank/mistakes.md`.
   - Nếu đưa ra quyết định kiến trúc mới, hãy lưu vào `memory-bank/decisions.md`.

---

## 2. QUY TRÌNH PHÁT TRIỂN & VIẾT CODE
Bạn phải tuân thủ quy trình phát triển có kế hoạch (Planning Mode):

1. **Lập kế hoạch (Planning Phase)**:
   - Nghiên cứu codebase kỹ lưỡng trước khi thay đổi.
   - Tạo/Cập nhật tài liệu kế hoạch triển khai (`implementation_plan.md` trong thư mục artifact) đối với các thay đổi lớn.
   - Nhận phản hồi và sự đồng ý từ User trước khi sửa code.

2. **Viết code (Implementation Phase)**:
   - Viết code sạch, dễ đọc, tuân thủ `memory-bank/coding-style.md`.
   - Giữ lại các chú thích (comments), docstrings hiện tại không liên quan đến thay đổi của bạn để tránh làm mất tài liệu nội bộ.
   - Sử dụng các link markdown dạng `file:///...` khi đề cập đến các tệp hoặc hàm trong phản hồi cho User.

3. **Xác minh (Verification Phase)**:
   - Kiểm tra kỹ code chạy được, chạy các câu lệnh test tự động (nếu có).
   - Viết/Cập nhật file `walkthrough.md` trong artifact để mô tả những thay đổi bạn đã thực hiện.

---

## 3. LƯU Ý ĐẶC BIỆT KHI CÀI ĐẶT
- Luôn kiểm tra xem thư mục hoặc file đã tồn tại chưa trước khi tạo mới.
- Không tự ý thay đổi thư viện cốt lõi hoặc cập nhật phiên bản lớn (major version) của dependencies nếu không có sự đồng ý của User.
- Khi giao tiếp với User, giữ câu trả lời ngắn gọn, tập trung và chuyên nghiệp.

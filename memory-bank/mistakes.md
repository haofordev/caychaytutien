# NHẬT KÝ LỖI TỪNG GẶP (MISTAKES & PITFALLS)

Tài liệu này ghi lại các lỗi lập trình quan trọng đã từng xảy ra trong hệ thống, nguyên nhân và cách phòng tránh để đảm bảo các AI khác và lập trình viên không lặp lại lỗi cũ.

---

## 1. LỖI RACE CONDITION KHI SPAM ĐĂNG KÝ TU LUYỆN / NHẬN THƯỞNG
* **Mô tả lỗi**: Người chơi dùng script click spam nhanh liên tiếp nhiều lần vào nút "Đột phá" hoặc "Nhận thưởng" khiến hệ thống xử lý song song nhiều request cùng lúc, dẫn đến việc được cộng thưởng nhân đôi hoặc tăng cấp vượt cấp trái quy định.
* **Nguyên nhân**: Hệ thống check điều kiện (ví dụ: `if (tuVi >= requiredTuVi)`) trước khi DB kịp lưu trạng thái mới (chưa bị trừ tu vi hoặc chưa đánh dấu đã nhận).
* **Cách khắc phục**:
  * Sử dụng cơ chế lock. Đối với Redis, dùng thư viện Redlock hoặc cơ chế phân tán lock theo `userId`.
  * Trong MongoDB, sử dụng transaction hoặc dùng câu lệnh `findOneAndUpdate` có điều kiện atomic (ví dụ: `{$set: {claimed: true}, $find: {claimed: false}}`).

---

## 2. BẢNG XẾP HẠNG TRÊN REDIS BỊ LỆCH SO VỚI MONGO DATABASE
* **Mô tả lỗi**: Điểm tu vi của người chơi trong hồ sơ cá nhân hiển thị một đằng, nhưng trên Bảng xếp hạng tuần lại hiển thị một nẻo hoặc không cập nhật.
* **Nguyên nhân**: Lập trình viên chỉ cập nhật trường `tuVi` trong MongoDB mà quên không gọi hàm đồng bộ hóa (`zadd`) lên Redis, hoặc quá trình gọi sang Redis bị crash nhưng không được handle/retry.
* **Cách khắc phục**:
  * Viết một service wrapper duy nhất cho việc cập nhật tu vi, ví dụ `cultivationService.updateTuVi(userId, newAmount)`. Hàm này sẽ chịu trách nhiệm cập nhật đồng thời cả Mongo và Redis.
  * Thiết lập một cron job tự động đồng bộ (sync job) chạy mỗi 24 giờ để đối chiếu cơ sở dữ liệu Mongo và Redis, sửa các bản ghi bị lệch.

---

## 3. LỆCH MÚI GIỜ CHẠY CRON JOB PHÁT THƯỞNG TUẦN (TIMEZONE MISMATCH)
* **Mô tả lỗi**: Phần thưởng tuần đáng lẽ phải trao lúc 23:59:59 Chủ Nhật (giờ Việt Nam, GMT+7) nhưng lại chạy lúc 06:59:59 sáng Thứ Hai hoặc muộn hơn.
* **Nguyên nhân**: Server deploy chạy trên hệ thống Docker/Cloud có múi giờ mặc định là UTC (GMT+0) khiến cron schedule chạy lệch 7 tiếng.
* **Cách khắc phục**:
  * Luôn chỉ định múi giờ rõ ràng khi cấu hình cron job (ví dụ sử dụng package `node-cron` hoặc `cron` hỗ trợ timezone, set timezone là `"Asia/Ho_Chi_Minh"`).
  * Viết log thời gian chạy ở cả dạng Local time và UTC time để dễ đối chiếu.

---

## 4. LỖI THẬP PHÂN KHI TÍNH TOÁN TỶ LỆ RƠI ĐỒ (FLOATING POINT PRECISION)
* **Mô tả lỗi**: Tỷ lệ rơi bản đồ kho báu là `5%` (`0.05`), nhưng sau khi cộng dồn các chỉ số may mắn, tỷ lệ ngẫu nhiên cho ra kết quả sai lệch hoặc không bao giờ rơi đồ.
* **Nguyên nhân**: Sử dụng phép so sánh trực tiếp số thực trong JavaScript (ví dụ: `0.1 + 0.2 === 0.3` trả về `false`).
* **Cách khắc phục**:
  * Chuyển tất cả tỷ lệ về dạng số nguyên (integer) khi tính toán ngẫu nhiên (ví dụ: nhân tỷ lệ với `10000` để tính phần vạn - vạn phân suất / basis points. Tỷ lệ 5% tương ứng với `500` điểm trên `10000`).
  * Sử dụng hàm random: `Math.floor(Math.random() * 10000) < dropChanceBasisPoints`.

# QUY CHUẨN API (API CONVENTION)

Tài liệu này quy định cách thiết kế và triển khai các API (Application Programming Interface) phục vụ việc giao tiếp
giữa Client (Frontend, Mobile app) và Backend Server **Phàm Nhân**.

---

## 1. PHƯƠNG THỨC HTTP & ĐƯỜNG DẪN (METHODS & ENDPOINTS)
* Tất cả API phải bắt đầu bằng tiền tố `/api/v1/`.
* Sử dụng danh từ số nhiều cho các tài nguyên (resources).
* **Quy chuẩn phương thức**:
* `GET`: Lấy thông tin (không thay đổi trạng thái máy chủ).
* `POST`: Tạo mới tài nguyên hoặc kích hoạt một hành động game (ví dụ: tu luyện, đi phụ bản).
* `PUT` / `PATCH`: Cập nhật thông tin.
* `DELETE`: Xóa tài nguyên.

### Các Endpoint chính dự kiến:
* `/api/v1/auth/login` (POST): Đăng nhập.
* `/api/v1/player/profile` (GET): Lấy thông tin tu vi, cảnh giới, túi đồ của người chơi.
* `/api/v1/cultivation/train` (POST): Kích hoạt hành động tu luyện.
* `/api/v1/cultivation/breakthrough` (POST): Thực hiện đột phá cảnh giới.
* `/api/v1/dungeons/enter` (POST): Đi phụ bản.
* `/api/v1/rewards/weekly` (GET): Xem trạng thái phần thưởng tuần của bản thân.
* `/api/v1/leaderboard/tuvi` (GET): Xem bảng xếp hạng tu vi toàn server.

---

## 2. ĐỊNH DẠNG PHẢN HỒI CHUẨN (STANDARD RESPONSE FORMAT)

### A. Phản hồi Thành Công (Success Response - 200 OK, 201 Created)
Mọi response thành công đều phải trả về đối tượng JSON có thuộc tính `success: true`.
```json
{
"success": true,
"message": "Thao tác thành công",
"data": {
"userId": "usr_67890",
"tuVi": 15200,
"level": "Trúc Cơ Tầng 1",
"rewardsReceived": [
{ "itemId": "item_treasure_map", "quantity": 1 }
]
}
}
```

### B. Phản hồi Lỗi (Error Response - 4xx, 5xx)
Mọi response lỗi đều phải trả về mã HTTP Status Code tương ứng và cấu trúc lỗi chuẩn để Client dễ hiển thị thông báo.
```json
{
"success": false,
"error": {
"code": "INSUFFICIENT_TUVI",
"message": "Không đủ tu vi để thực hiện đột phá cảnh giới."
}
}
```

---

## 3. XÁC THỰC NGƯỜI CHƠI (AUTHENTICATION)
* Xác thực bằng **JSON Web Token (JWT)**.
* Token được gửi kèm trong Header của request với định dạng:
`Authorization: Bearer <token_string>`
    * Token hết hạn sẽ trả về HTTP Status Code `401 Unauthorized`.
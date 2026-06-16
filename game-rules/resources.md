# QUY TẮC GAME: PHÂN PHỐI TÀI NGUYÊN CHUNG VÀ TÀI NGUYÊN RIÊNG

Tài liệu này quy định cách phân tách dữ liệu game giữa các hoạt động cá nhân biệt lập (Private Instance) và các tài nguyên cạnh tranh dùng chung trên toàn máy chủ (Global/Shared Resources).

---

## 1. TÀI NGUYÊN RIÊNG BIỆT (PRIVATE INSTANCES)

Tài nguyên riêng là những tài nguyên thuộc quyền sở hữu độc quyền của một người chơi, tiến trình và dữ liệu không bị can thiệp bởi người chơi khác.

### 1.1. Bản thân nhân vật
* **Dữ liệu lưu trữ**: Cảnh giới, Tu vi hiện tại, Tuổi tác, Thọ nguyên tối đa, và Điểm Chân Linh luân hồi.
* **Túi đồ cá nhân**: Toàn bộ Linh thạch, Đan dược, Pháp bảo, Sách công pháp và Nguyên liệu thô nằm trong túi đồ của người chơi là bảo mật và không thể bị người khác xem hoặc lấy trộm trực tiếp (trừ khi có tính năng giao dịch tự nguyện).

### 1.2. Bí Cảnh Phong Ấn (Leo Tháp PVE)
* **Cơ chế hoạt động**:
  * Mỗi người chơi sở hữu một tiến trình leo ải Bí Cảnh riêng biệt.
  * Việc người chơi A vượt qua Ải 50 không khóa hay ảnh hưởng đến tiến trình vượt Ải của người chơi B.
  * Phần thưởng vượt ải lần đầu (First Clearance Reward) là cố định và phát cho riêng từng người chơi khi họ vượt qua ải đó.
  * Không giới hạn số lượng người chơi có thể vượt ải cùng một thời điểm.

---

## 2. TÀI NGUYÊN DÙNG CHUNG & TRANH ĐOẠT (GLOBAL SHARED RESOURCES)

Tài nguyên dùng chung là các tài nguyên hữu hạn được phân bổ trên toàn máy chủ. Người chơi bắt buộc phải cạnh tranh để giành quyền khai thác.

### 2.1. Mỏ Khai Thác Khoáng Thạch & Linh Mạch (PVP Resource Nodes)
* **Khái niệm**: Linh Mạch là các mỏ tập trung linh khí xuất hiện ngẫu nhiên trên bản đồ thế giới của Server.
* **Phân cấp mỏ**:
  * **Linh Mạch Cực Phẩm** (Tối đa 5 mỏ toàn server): Tăng $+300\%$ tốc độ tu luyện tĩnh tọa, sản lượng đào khoáng $+100\%$.
  * **Linh Mạch Thượng Phẩm** (Tối đa 15 mỏ toàn server): Tăng $+150\%$ tốc độ tu luyện tĩnh tọa, sản lượng đào khoáng $+50\%$.
  * **Linh Mạch Trung Phẩm** (Tối đa 50 mỏ toàn server): Tăng $+50\%$ tốc độ tu luyện tĩnh tọa, sản lượng đào khoáng $+20\%$.
* **Quy tắc Tranh Đoạt**:
  1. Người chơi có thể bấm "Chiếm Đóng" một mỏ trống bất kỳ trên bản đồ thế giới.
  2. Nếu mỏ đã bị người khác chiếm đóng, người chơi có thể gửi lệnh thách đấu **PVP Tự Động**.
  3. **Kết quả PVP**:
     * Hệ thống tính toán sát thương dựa trên Cảnh giới, Thần thông (Đạo Tu), Pháp bảo phòng ngự (Thể Tu), Ma công khống chế (Ma Tu) và thuộc tính Pet mang theo.
     * Người thắng cuộc giành quyền chiếm giữ mỏ. Người thua cuộc bị đẩy ra ngoài và nhận trạng thái hồi chiêu chiếm mỏ (3 phút).
  4. **Giới hạn thời gian**: Một người chơi chỉ được chiếm giữ một mỏ tối đa **4 giờ liên tục** mỗi ngày để tránh tình trạng độc chiếm tài nguyên bởi đại năng cấp cao. Sau 4 giờ, hệ thống tự động đẩy người chơi ra để nhường chỗ cho người khác.

### 2.2. Giới Hạn Tài Nguyên Server Mỗi Ngày (Global Caps)
Vì linh khí cạn kiệt, mỗi ngày hệ thống chỉ tự động sinh ra một lượng tài nguyên hữu hạn cho toàn server:
* **Linh khí tự nhiên**: 1,000,000 EXP (Tĩnh tọa vượt mốc này sẽ bị giảm tốc độ nhận tu vi còn 10% cơ bản).
* **Linh dược dã ngoại**: 10,000 gốc (Thu hoạch từ Giang Hồ).
* **Khoáng thạch thô**: 5,000 quặng.
* **Yêu thú cấp cao**: 1,000 con (Phục vụ săn bắn đoạt yêu đan).

Khi lượng tài nguyên toàn server bị khai thác hết trong ngày (đạt giới hạn cap), các hoạt động tương ứng của người chơi (Săn bắn, Khai khoáng, Du ngoạn) sẽ bị giảm $90\%$ sản lượng nhận được cho đến khi bước sang ngày tiếp theo (Server reset lúc 00:00).

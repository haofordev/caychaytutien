# QUY TẮC GAME: PHÂN PHỐI TÀI NGUYÊN CHUNG VÀ TÀI NGUYÊN RIÊNG

Tài liệu này quy định cách phân tách dữ liệu game giữa các hoạt động cá nhân biệt lập (Private Instance) và các tài nguyên cạnh tranh dùng chung trên toàn máy chủ (Global/Shared Resources).

---

## 1. TÀI NGUYÊN RIÊNG BIỆT (PRIVATE INSTANCES)

Tài nguyên riêng là những tài nguyên thuộc quyền sở hữu độc quyền của một người chơi, tiến trình và dữ liệu không bị can thiệp bởi người chơi khác.

### 1.1. Bản thân nhân vật
* **Dữ liệu lưu trữ**: Cảnh giới, Tu vi hiện tại, Tuổi tác, Thọ nguyên tối đa, thể lực hiện tại/tối đa, HP hiện tại/tối đa, và Điểm Chân Linh luân hồi.
* **Túi đồ cá nhân**: Toàn bộ Linh thạch, Đan dược, Pháp bảo, Sách công pháp và Nguyên liệu thô nằm trong túi đồ của người chơi là bảo mật và không thể bị người khác xem hoặc lấy trộm trực tiếp (trừ khi có tính năng giao dịch tự nguyện).

### 1.2. Sân nhà Thanh Vân và tài nguyên nhập môn
Mọi người chơi bắt đầu là Phàm Nhân và có một khu sinh kế riêng tại Thanh Vân Thôn:
* **Ô trồng linh dược thô**: nguồn dược liệu thấp cấp để bán, luyện đan nhập môn hoặc nuôi linh thú.
* **Chuồng linh thú non**: nuôi 1 linh thú non đầu tiên, lấy nguyên liệu hoặc giữ làm pet sau khi nhập môn.
* **Mỏ khoáng cạn**: khai thác khoáng thạch thô và linh thạch vụn; mỗi lượt tiêu hao thể lực.
* **Bí cảnh ngoại vi**: săn yêu thú yếu; tiêu hao thể lực/HP và có cơ hội nhận yêu đan vỡ, thú non, tàn quyển công pháp.

Tài nguyên từ sân nhà và bí cảnh ngoại vi thuộc cá nhân, không bị người chơi khác tranh đoạt.

### 1.3. Dược Viên, Mỏ Khoáng và Bí Cảnh theo tầng
Sau khi học **Dẫn Khí Nhập Thể Quyết**, người chơi mở Thông Thiên Động Phủ Tầng 1. Mỗi tầng có bộ tài nguyên cá nhân riêng:
* **Dược Viên tầng**: trồng linh dược đúng phẩm cấp tầng; Đạo Tu tăng tỷ lệ trồng thành công và phẩm chất thu hoạch.
* **Mỏ Khoáng tầng**: khai khoáng cá nhân; Thể Tu tăng thể lực, giảm tiêu hao thể lực và tăng sản lượng.
* **Bí Cảnh tầng**: săn bắn cá nhân; Ma Tu hút HP khi gây sát thương, giảm hao tổn HP và tăng tỷ lệ rơi Yêu Đan.

Các tài nguyên này không cạnh tranh trực tiếp giữa người chơi, nhưng bị giới hạn bởi thể lực, HP, thời gian sinh trưởng, thời gian hồi bí cảnh và phẩm cấp tầng.

### 1.4. Bí Cảnh Phong Ấn (Leo Tháp PVE)
* **Cơ chế hoạt động**:
  * Mỗi người chơi sở hữu một tiến trình leo ải Bí Cảnh riêng biệt.
  * Việc người chơi A vượt qua Ải 50 không khóa hay ảnh hưởng đến tiến trình vượt Ải của người chơi B.
  * Phần thưởng vượt ải lần đầu (First Clearance Reward) là cố định và phát cho riêng từng người chơi khi họ vượt qua ải đó.
  * Không giới hạn số lượng người chơi có thể vượt ải cùng một thời điểm.

---

## 2. TÀI NGUYÊN DÙNG CHUNG & TRANH ĐOẠT (GLOBAL SHARED RESOURCES)

Tài nguyên dùng chung là các tài nguyên hữu hạn được phân bổ trên toàn máy chủ. Người chơi bắt buộc phải cạnh tranh để giành quyền khai thác.

### 2.1. Linh Mạch Tranh Đoạt (PVP Resource Nodes)
* **Khái niệm**: Linh Mạch là các mỏ tập trung linh khí xuất hiện ngẫu nhiên trên bản đồ thế giới của Server. Đây là tài nguyên tranh đoạt toàn server, khác với mỏ khoáng cá nhân trong sân nhà hoặc Động Phủ tầng.
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

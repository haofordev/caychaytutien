# QUY TẮC GAME: THÔNG THIÊN ĐỘNG PHỦ (PHÂN TẦNG)

Tài liệu này quy định chi tiết cơ chế phân tầng xã hội của Động Phủ, cách mua ô đất, giới hạn 100 ô/tầng, điều kiện lên tầng, và các hoạt động sản xuất Linh Điền (trồng dược), Yêu Vực (nuôi thú).

---

## 1. CƠ CHẾ PHÂN TẦNG & GIAO DỊCH Ô ĐẤT

Do linh khí thiên địa cạn kiệt, các tu sĩ mạt pháp phải tập trung xây dựng **Thông Thiên Tháp Động Phủ** nhằm hội tụ linh khí từ linh mạch sâu trong lòng đất.

### 1.1. Cấu trúc và Giới hạn ô đất
* **Phân tầng**: Tháp có nhiều tầng (Floor 1, 2, 3...). Tầng càng cao thì càng gần nguồn năng lượng lọc sạch, linh khí càng đậm đặc.
* **Giới hạn**: Mỗi tầng chỉ chứa đúng **100 ô động phủ** (tương ứng với các vị trí từ `1` đến `100`).
* **Sở hữu**: Mỗi người chơi chỉ được phép sở hữu **duy nhất 1 ô động phủ** trên toàn bộ hệ thống tháp tại một thời điểm.

### 1.2. Mua ô đất và Bảng giá theo tầng
Người chơi đạt **Luyện Khí Tầng 5** mới đủ tư cách mua ô đất đầu tiên ở Tầng 1.

Giá mua ô đất tăng lũy tiến theo tầng để lọc bớt những tu sĩ nghèo khó hoặc tu vi thấp:

$$Price_{floor} = Price_{base} \times 2^{floor - 1}$$

* Với $Price_{base} = 1,000$ Linh thạch (cho Tầng 1).
* Bảng chi phí mua ô:
  * **Tầng 1**: 1,000 Linh thạch.
  * **Tầng 2**: 2,000 Linh thạch.
  * **Tầng 3**: 4,000 Linh thạch.
  * **Tầng 4**: 8,000 Linh thạch.
  * **Tầng 5**: 16,000 Linh thạch.
  * *(Tiếp tục nhân đôi mỗi tầng)*

---

## 2. QUY TẮC DỊCH CHUYỂN LÊN TẦNG TRÊN (UPGRADE FLOOR)

Khi người chơi tích lũy đủ tu vi và tiền bạc, họ có thể yêu cầu nâng cấp động phủ để chuyển lên tầng cao hơn.

### 2.1. Điều kiện chuyển tầng
1. **Yêu cầu Cảnh giới**: Tầng càng cao yêu cầu cảnh giới tu vi càng lớn:
   * **Tầng 1 $\rightarrow$ 2**: Cảnh giới Luyện Khí Tầng 5 trở lên.
   * **Tầng 3 $\rightarrow$ 4**: Cảnh giới Trúc Cơ Sơ Kỳ trở lên.
   * **Tầng 5 $\rightarrow$ 6**: Cảnh giới Kim Đan Sơ Kỳ trở lên.
   * *(Mỗi 2 tầng yêu cầu bậc cảnh giới lớn tiếp theo)*
2. **Số ô trống khả dụng**: Tầng đích đến phải có ít nhất 1 ô trống (Tổng số ô đã mua trên tầng đó < 100).
   * **NẾU TẦNG ĐẦY (100/100 ô)**: Nút "Lên Tầng" của tầng đó sẽ bị **Khóa (Full)**. Người chơi bắt buộc phải đợi có người chơi khác chuyển đi (lên tầng cao hơn nữa hoặc luân hồi giải phóng ô) thì mới có thể mua.
3. **Phí chuyển tầng**: Trả $100\%$ giá mua ô của tầng mới. 
   * Hệ thống tự động thu hồi ô cũ ở tầng dưới và **hoàn trả 50%** giá mua của ô cũ vào túi đồ của người chơi. Toàn bộ tài nguyên đang gieo trồng/nuôi dưỡng sẽ được tự động vận chuyển sang ô mới an toàn.

### 2.2. Hiệu ứng Buff của Tầng Động Phủ
Sở hữu ô đất ở tầng cao mang lại lợi ích cực lớn cho tu hành:
* **Tốc độ hấp thu linh khí**: Mỗi cấp của Tầng cộng vĩnh viễn **+10%** tốc độ tu luyện tĩnh tọa cơ bản ($Bonus_{abode\_floor} = floor \times 0.1$).
  * Tầng 1: +10%
  * Tầng 5: +50%
  * Tầng 10: +100%

---

## 3. CÁC HOẠT ĐỘNG TRONG Ô ĐỘNG PHỦ

Sau khi mua thành công 1 ô đất, người chơi sẽ được cấp hai phân khu chức năng riêng:

### 3.1. Linh Điền (Trồng Thảo Dược)
* **Quy mô**: 6 ô đất trồng độc lập.
* **Quy trình**:
  1. Gieo hạt giống thảo dược (Tụ Linh Thảo, Trúc Cơ Hoa, Tẩy Tủy Chi).
  2. Thời gian đếm ngược sinh trưởng (Ví dụ: Tụ Linh Thảo cần 2 giờ). Hệ Đạo Tu có thiên phú giảm 50% thời gian này.
  3. Thu hoạch: Nhận Linh dược thô dùng để chế tạo đan dược tại Đan Phòng.
* **Rủi ro**: Nếu ô đất động phủ nằm ở tầng quá thấp (Tầng 1-2), có tỷ lệ $5\%$ linh dược bị sâu bệnh làm giảm $20\%$ sản lượng khi thu hoạch. Tầng càng cao tỷ lệ sâu bệnh càng giảm về 0%.

### 3.2. Yêu Vực (Nuôi Thú)
* **Quy mô**: 3 chuồng nuôi yêu thú.
* **Quy trình**:
  1. Trong quá trình săn bắn (Ma Tu) hoặc du ngoạn kỳ ngộ, người chơi có tỷ lệ bắt được Yêu thú non (ví dụ: *Linh Thử*, *Hỏa Tước*, *Thiết Ngưu*).
  2. Mang thú vào chuồng nuôi. Hằng ngày phải cho ăn bằng khoáng sản cặn (Thể Tu) hoặc linh dược thừa để tăng độ trưởng thành.
  3. Khi thú đạt **Trưởng Thành (100% tiến độ)**:
     * *Thu hoạch nguyên liệu*: Lấy máu thú, da thú, yêu cốt để rèn pháp bảo hoặc luyện đan.
     * *Thuần hóa thành Trợ Chiến (Pet)*: Trang bị thú nuôi vào khay Pet giúp cộng trực tiếp chỉ số thuộc tính cho nhân vật (+5% HP hoặc +5% Tấn công khi PK chiếm mỏ).

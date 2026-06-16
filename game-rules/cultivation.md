# QUY TẮC GAME: TU LUYỆN, CẢNH GIỚI VÀ TIẾN TRÌNH NHÂN VẬT

Tài liệu này quy định chi tiết các công thức toán học và logic vận hành của hệ thống Tu Luyện, Đột Phá Thiên Kiếp, Thọ Nguyên và Luân Hồi Chuyển Thế.

---

## 1. CƠ CHẾ TÍCH LŨY EXP (TU VI)

Người chơi tích lũy Tu Vi thông qua hành động **Tĩnh Tọa Hấp Thu** (chủ động hoặc offline tối đa 8 giờ).

### 1.1. Công thức tính Tu Vi mỗi giây (EXP/s)
Tốc độ tăng tu vi cuối cùng của nhân vật được tính theo công thức:

$$Speed_{final} = Speed_{base} \times (1 + Bonus_{cong\_phap} + Bonus_{linh\_can} + Bonus_{abode\_floor}) \times Buff_{linh\_mach}$$

Trong đó:
* $Speed_{base} = 1$ EXP/giây (hằng số linh khí cơ bản thời Mạt Pháp).
* $Bonus_{cong\_phap}$: Phần trăm tăng thêm từ công pháp đang trang bị (ví dụ: *Thanh Mộc Quyết* là `+1.0` hay `+100%`).
* $Bonus_{linh\_can}$: Tăng thêm từ phẩm chất Linh Căn (ví dụ: Tạp linh căn +0%, Song linh căn +50%, Thiên linh căn +150%). Phẩm chất Linh căn được nâng cấp bằng Chân Linh Điểm sau khi luân hồi.
* $Bonus_{abode\_floor}$: Tăng thêm từ tầng Động Phủ đang sở hữu (Thông Thiên Động Phủ). Mỗi tầng tăng **+10%** ($+0.1$) tốc độ hấp thu (ví dụ: Tầng 10 tăng +100%).
* $Buff_{linh\_mach}$: Hệ số nhân nếu người chơi chiếm giữ thành công mỏ Linh Mạch cực phẩm dùng chung trên bản đồ thế giới. Mặc định là $1.0$, nếu đang chiếm mỏ thì hệ số nhân là **$3.0$** ($300\%$).

---

## 2. BẢNG CẢNH GIỚI VÀ YÊU CẦU EXP ĐỘT PHÁ

Dưới đây là các mốc tu vi (EXP) tích lũy cần thiết để đột phá lên cấp độ tiếp theo:

| Cảnh Giới lớn | Tầng cảnh giới | Yêu cầu EXP | Thọ Nguyên tối đa (năm) | Ghi chú |
| :--- | :--- | :--- | :--- | :--- |
| **Phàm Nhân** | Tầng duy nhất | 100 | 100 | Tĩnh tọa đạt 100 EXP để khảo nghiệm linh căn |
| **Luyện Khí** | Tầng 1 | 500 | 150 | Tốc độ cơ bản |
| | Tầng 2 | 1,000 | 150 | |
| | Tầng 3 | 2,500 | 150 | |
| | Tầng 4 | 5,000 | 150 | |
| | Tầng 5 | 10,000 | 150 | Mở khóa Động Phủ (mua ô Tầng 1) |
| | Tầng 6 | 20,000 | 150 | |
| | Tầng 7 | 40,000 | 150 | |
| | Tầng 8 | 80,000 | 150 | |
| | Tầng 9 (Mốc) | 150,000 | 150 | Đạt 100% kích hoạt Đột Phá Lôi Kiếp Trúc Cơ |
| **Trúc Cơ** | Sơ Kỳ | 300,000 | 300 | Tăng thọ nguyên lên 300 tuổi |
| | Trung Kỳ | 600,000 | 300 | |
| | Hậu Kỳ | 1,200,000 | 300 | |
| | Viên Mãn (Mốc) | 2,500,000 | 300 | Đạt 100% kích hoạt Đột Phá Lôi Kiếp Kim Đan |
| **Kim Đan** | Sơ Kỳ | 5,000,000 | 600 | Tăng thọ nguyên lên 600 tuổi |
| | Trung Kỳ | 10,000,000 | 600 | |
| | Hậu Kỳ | 20,000,000 | 600 | |
| | Viên Mãn (Mốc) | 40,000,000 | 600 | |
| **Nguyên Anh** | Sơ -> Viên Mãn | Lũy thừa x2 | 1,200 | |
| **Hóa Thần** | Sơ -> Viên Mãn | Lũy thừa x2 | 2,400 | |
| **Luyện Hư** | Sơ -> Viên Mãn | Lũy thừa x2 | 4,800 | |
| **Hợp Thể** | Sơ -> Viên Mãn | Lũy thừa x2 | 9,600 | |
| **Đại Thừa** | Sơ -> Viên Mãn | Lũy thừa x2 | 19,200 | |
| **Độ Kiếp** | Phi Thăng | 1,000,000,000 | Vô hạn | Vượt ải thành công sẽ chiến thắng game |

---

## 3. CƠ CHẾ ĐỘT PHÁ VÀ THIÊN KIẾP (LÔI KIẾP)

Đột phá cảnh giới lớn (ví dụ: Luyện Khí Tầng 9 $\rightarrow$ Trúc Cơ Sơ Kỳ) sẽ kích hoạt Lôi Kiếp. 

### 3.1. Các thông số lôi kiếp cơ bản
* **Tỷ lệ thành công mặc định ($Rate_{default}$)**:
  * Lên Trúc Cơ: **50%**
  * Lên Kim Đan: **40%**
  * Lên Nguyên Anh: **30%**
  * Lên Hóa Thần trở lên: **15%**
* **Tổng tỷ lệ thành công thực tế ($Rate_{final}$)**:
  $$Rate_{final} = Rate_{default} + Bonus_{dan\_duoc} + Bonus_{phap\_bao} + Bonus_{tran\_phap}$$
  *(Lưu ý: Tỷ lệ $Rate_{final}$ tối đa đạt $100\%$)*

### 3.2. Rủi ro khi Đột phá Thất bại
Nếu kết quả ngẫu nhiên rơi vào thất bại ($100\% - Rate_{final}$):
1. **30% Trọng thương**:
   * Nhân vật bị trừ ngay lập tức **20%** số lượng Tu Vi (EXP) tích lũy của tầng hiện tại.
   * Gắn hiệu ứng trạng thái "Trọng Thương Lôi Kiếp": Giảm **50%** tốc độ hấp thu tu vi trong **2 giờ** (thời gian thực tế). Có thể dùng *Hồi Linh Đan* hoặc *Tẩy Tủy Đan* để xóa bỏ trạng thái này lập tức.
2. **20% Thân Tử Đạo Tiêu (Chết)**:
   * Thể xác tiêu biến vĩnh viễn. Nhân vật bị đưa vào trạng thái **Luân Hồi Chuyển Thế**.

---

## 4. HỆ THỐNG THỌ NGUYÊN & LUÂN HỒI (CƠ CHẾ SINH TỒN)

### 4.1. Cách tính Tuổi tác và Thọ nguyên
* **Quy đổi thời gian**: 1 giờ ngoài đời thực = 1 năm tuổi trong game.
* Mỗi giây trôi qua, tuổi nhân vật tăng thêm: $1 / 3600$ tuổi.
* Khi tuổi nhân vật hiện tại vượt quá `maxAge` (Thọ nguyên tối đa của cảnh giới hiện tại), nhân vật sẽ **Chết già** và tự động kích hoạt Luân Hồi Chuyển Thế khi người chơi đăng nhập hoặc tương tác.

### 4.2. Công thức tính Chân Linh Điểm khi Luân Hồi
Khi nhân vật chết (do lôi kiếp hoặc chết già), người chơi nhận được Chân Linh Điểm để kế thừa sang kiếp sau:

$$Chân\_Linh\_Điểm = (Cảnh\_Giới\_Index \times 10) + (ReincarnationCnt \times 2)$$

Trong đó:
* `Cảnh_Giới_Index` là chỉ số thứ tự của cảnh giới lớn đã đạt được kiếp trước (Phàm Nhân = 0, Luyện Khí = 1, Trúc Cơ = 2, Kim Đan = 3, v.v.).
* `ReincarnationCnt` là số lần người chơi đã luân hồi trước đó (khuyến khích người chơi kiên trì tái sinh).

### 4.3. Tiêu dùng Chân Linh Điểm
Người chơi dùng điểm này trước khi bắt đầu nhân vật mới để nâng cấp Linh Căn:
* **Tạp Linh Căn** (Mặc định): Tốc độ tu luyện $+0\%$.
* **Tam Linh Căn** (Giá: 10 Chân Linh): Tốc độ tu luyện $+20\%$.
* **Song Linh Căn** (Giá: 30 Chân Linh): Tốc độ tu luyện $+60\%$.
* **Thiên Linh Căn** (Giá: 80 Chân Linh): Tốc độ tu luyện $+150\%$.
* **Băng/Lôi Dị Linh Căn** (Giá: 150 Chân Linh): Tốc độ tu luyện $+300\%$, tăng $10\%$ tỷ lệ thành công lôi kiếp vĩnh viễn.
* **Di sản đem theo**: Mua quyền mang theo 1 cuốn công pháp kiếp trước đã học (Giá: 20 Chân Linh).

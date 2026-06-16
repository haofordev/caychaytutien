# TÀI LIỆU THIẾT KẾ TRÒ CHƠI: PHÀM NHÂN TU TIÊN (GAME DESIGN DOCUMENT)

* **Tên trò chơi (Đề xuất):** Phàm Nhân Tu Tiên: Mạt Pháp Chi Lộ
* **Thể loại:** Web Game mô phỏng tu tiên, Idle/Incremental, RPG sinh tồn, Text-based kết hợp đồ họa gọn nhẹ.
* **Định dạng hiển thị:** Màn hình dọc (Portrait UI - Mobile-first), tối ưu hóa trải nghiệm trên thiết bị di động.

---

## 1. CỐT TRUYỆN & BỐI CẢNH THẾ GIỚI

### 1.1. Thượng Cổ Huy Hoàng và Trận Tiên Ma Đại Chiến
Vạn năm trước, thế giới tu tiên nằm trong trạng thái **Thiên Đạo hoàn chỉnh**. Linh khí nồng đậm bao phủ đại địa, đại năng tu sĩ nhiều vô số kể. Họ có thể "dời non lấp biển", "hái sao bắt trăng", thọ mệnh đồng trời đất, phi thăng tiên giới chỉ trong chớp mắt.

Tuy nhiên, lòng tham và mâu thuẫn giữa hai phe Tiên - Ma đã dẫn đến cuộc **Đại Chiến Tiên Ma** chấn động tam giới. Trận chiến hủy thiên diệt địa này đã đánh vỡ quy tắc Thiên Đạo, linh mạch toàn cầu bị đứt gãy, Tiên giới phong tỏa lối đi. Đại địa vỡ vụn thành vô số mảnh nhỏ, tạo ra các bí cảnh phong ấn.

### 1.2. Kỷ Nguyên Mạt Pháp
Bước vào thời đại ngày nay, thế giới chìm trong **Mạt Pháp thời kỳ**:
* **Linh khí cạn kiệt:** Nồng độ linh khí trong thiên địa chỉ còn **1%** so với thời Thượng cổ. Tu luyện thông thường gần như không thể tiến triển.
* **Công pháp thất truyền:** Các công pháp cổ cấp cao bị rách nát, thất lạc trong chiến hỏa.
* **Đan phương chia cắt:** Kỹ thuật luyện đan thượng cổ bị phân tán, thảo dược biến dị khó sinh trưởng.
* **Độc quyền tài nguyên:** Các tông môn lớn còn sót lại kiểm soát các linh mạch tốt nhất, phong tỏa tài nguyên, phàm nhân muốn tu tiên gần như không có cơ hội.

---

## 2. KHỞI ĐẦU NGƯỜI CHƠI & 3 HỆ TU HÀNH

Người chơi xuất thân là một phàm nhân sinh sống tại **Thanh Vân Thôn** - một ngôi làng hẻo lánh dưới chân núi. Một đêm nọ, một **Thiên Ngoại Dị Bảo** (Linh Bảo Vô Danh) từ trên trời rơi xuống và dung nhập vào đan điền người chơi, đánh thức **Linh Căn ẩn** và mở ra con đường tu hành. 

Tại đây, dựa trên duyên pháp và Linh căn khảo nghiệm, người chơi được lựa chọn 1 trong 3 con đường tu hành chính:

```
                      [ Người chơi khởi đầu: Phàm Nhân ]
                                      |
                     (Thiên Ngoại Dị Bảo - Khảo Nghiệm)
                                      |
         +----------------------------+----------------------------+
         |                            |                            |
  [ ⚔️ ĐẠO TU ]                 [ 🛡️ THỂ TU ]                 [ 🔥 MA TU ]
(Đạo Pháp - Linh Dược)        (Thân Pháp - Khoáng Thạch)    (Sát Phạt - Yêu Đan)
```

### ⚔️ Hệ 1: ĐẠO TU (Đạo Pháp Chi Đường)
* **Tuyên ngôn:** *"Dùng thiên địa chi lực, ngưng tụ thần thông vô thượng."*
* **Đặc điểm chiến đấu:** Công kích đơn thể mạnh nhất, sát thương bộc phát chí mạng cao, hấp thu linh khí tự nhiên hiệu quả hơn các hệ khác.
* **Thiên phú độc quyền: Dược Đạo Chi Tâm**
  * Tốc độ sinh trưởng của Linh dược trong Linh điền: **+50%**.
  * Tỷ lệ biến dị thảo dược khi gieo trồng: **+20%** (thu được dược liệu cực phẩm).
  * Tỷ lệ luyện đan thành công: **+15%**.
* **Vòng lặp phát triển cốt lõi:**
  $$\text{Linh Dược} \longrightarrow \text{Đan Dược} \longrightarrow \text{Tích lũy Tu Vi} \longrightarrow \text{Khai mở Thần Thông}$$

### 🛡️ Hệ 2: THỂ TU (Cực Hạn Thân Pháp)
* **Tuyên ngôn:** *"Lấy thân làm khí, lấy huyết làm lò, nhục thân bất hoại."*
* **Đặc điểm chiến đấu:** Lượng máu (HP) cực lớn, phòng thủ vật lý siêu việt, khả năng hồi phục máu liên tục trong trận đấu.
* **Thiên phú độc quyền: Bất Diệt Thánh Thể**
  * Sản lượng khoáng thạch khai thác trong Linh mạch: **+50%**.
  * Xác suất đào được Linh thạch hiếm (Linh thạch thượng phẩm): **+10%**.
  * Tốc độ rèn luyện thân thể (Luyện Thể) tăng tốc: **+20%**.
* **Vòng lặp phát triển cốt lõi:**
  $$\text{Khoáng Thạch} \longrightarrow \text{Pháp Bảo Hộ Thân} \longrightarrow \text{Luyện Thể cường hóa} \longrightarrow \text{Tăng bậc Cảnh Giới}$$

### 🔥 Hệ 3: MA TU (Huyết Sát Ma Công)
* **Tuyên ngôn:** *"Cướp đoạt sinh cơ của vạn vật, dùng sát phạt chứng đạo."*
* **Đặc điểm chiến đấu:** Sát thương diện rộng (AoE) mạnh nhất, farm quái/quái vật nhanh, sở hữu các kỹ năng khống chế (làm chậm, hút máu, nguyền rủa).
* **Thiên phú độc quyền: Huyết Sát Chi Thể**
  * Kinh nghiệm thu hoạch khi săn yêu thú: **+50%**.
  * Tỷ lệ rơi Yêu Đan từ quái vật: **+20%**.
  * Xác suất chạm trán Yêu thú Tinh anh/Boss (mang tài nguyên lớn): **+15%**.
* **Vòng lặp phát triển cốt lõi:**
  $$\text{Săn Quái thú} \longrightarrow \text{Đoạt Yêu Đan} \longrightarrow \text{Luyện Ma Công} \longrightarrow \text{Đột Phá Cảnh Giới}$$

---

## 3. HỆ THỐNG CẢNH GIỚI & ĐỘT PHÁ THIÊN KIẾP

### 3.1. Danh Sách Cảnh Giới
Mỗi cảnh giới yêu cầu một lượng Tu Vi tích lũy nhất định. Từ Luyện Khí đến Trúc Cơ bắt đầu mở khóa thêm các thuộc tính riêng biệt.

1. **Phàm Nhân** (Khởi đầu) $\rightarrow$ Đạt 100 Tu Vi để bắt đầu Khảo nghiệm Linh Căn.
2. **Luyện Khí** (Tầng 1 $\rightarrow$ Tầng 9): Bước đầu dẫn khí nhập thể.
3. **Trúc Cơ** (Sơ kỳ $\rightarrow$ Trung kỳ $\rightarrow$ Hậu kỳ $\rightarrow$ Viên Mãn): Đúc nền móng tiên đạo. Công pháp bắt đầu phân hóa ngũ hành (Kim, Mộc, Thủy, Hỏa, Thổ) và phẩm bậc (Hoàng $\rightarrow$ Huyền $\rightarrow$ Địa $\rightarrow$ Thiên).
4. **Kim Đan (Kết Đan)**: Ngưng tụ nội đan.
5. **Nguyên Anh**: Hóa đan thành anh nhi thần thức.
6. **Hóa Thần**: Thần thức xuất khiếu, hòa nhập trời đất.
7. **Luyện Hư**: Phân tách hư thực.
8. **Hợp Thể**: Nhục thân và nguyên thần hợp nhất.
9. **Đại Thừa**: Tiệm cận tiên nhân.
10. **Độ Kiếp Phi Thăng**: Vượt qua cửu thiên lôi kiếp để phi thăng Tiên Giới (Chiến thắng game).

### 3.2. Cơ Chế Đột Phá & Thiên Kiếp (Lôi Kiếp)
Mỗi lần người chơi muốn thăng cấp cảnh giới lớn (ví dụ: *Luyện Khí 9* $\rightarrow$ *Trúc Cơ Sơ kỳ* hoặc *Trúc Cơ Viên Mãn* $\rightarrow$ *Kim Đan*), họ phải đương đầu với **Thiên Kiếp (Lôi Kiếp)**.

* **Tỷ lệ thành công cơ bản:**
  * Cảnh giới thấp (Luyện Khí lên Trúc Cơ): **50%** thành công.
  * Cảnh giới trung (Trúc Cơ lên Kim Đan): **40%** thành công.
  * Cảnh giới cao (từ Nguyên Anh trở lên): Giảm dần còn **30% $\rightarrow$ 10%**.
* **Rủi ro khi thất bại:**
  * **30% Trọng thương:** Mất **20%** lượng tu vi hiện tại, bị giảm tốc độ hấp thu linh khí trong 2 giờ ngoài đời thực (trừ khi dùng *Hồi Linh Đan* hoặc *Tẩy Tủy Đan* để chữa trị).
  * **20% Thân Tử Đạo Tiêu (Tử vong):** Nhân vật chết, toàn bộ thể xác tiêu biến, buộc phải đi vào **Luân Hồi Chuyển Thế**.
* **Các phương án nâng tỷ lệ thành công (Chống Lôi Kiếp):**
  * **Đan Dược:** Cắn *Trúc Cơ Đan* (+30% tỷ lệ đột phá Trúc Cơ), *Phá Cảnh Đan* (+20% tỷ lệ đột phá Kết Đan).
  * **Pháp Bảo (Thể Tu rèn):** Trang bị *Khiên Tỵ Lôi*, *Giáp Huyền Thiết* giảm sát thương sấm sét.
  * **Trận Pháp (Động phủ):** Kích hoạt *Hộ Sơn Đại Trận* hoặc *Tụ Linh Trận* để hấp thu một phần uy lực lôi kiếp (+15% tỷ lệ thành công).

---

## 4. HỆ THỐNG THỌ NGUYÊN & LUÂN HỒI (CƠ CHẾ SINH TỒN)

Thời đại Mạt Pháp linh khí loãng làm giảm thọ mệnh của tu sĩ. Nếu không kịp đột phá cảnh giới để gia tăng thọ nguyên, tu sĩ sẽ tích lũy tuổi tác và **chết già**.

### 4.1. Giới Hạn Thọ Nguyên theo Cảnh Giới
* **Phàm Nhân:** 100 năm.
* **Luyện Khí:** 150 năm.
* **Trúc Cơ:** 300 năm.
* **Kim Đan:** 600 năm.
* **Nguyên Anh:** 1,200 năm.
* *(Mỗi cảnh giới lớn tiếp theo tăng gấp đôi thọ nguyên).*

### 4.2. Quy đổi Thời gian
* **Tỷ lệ:** 1 giờ thời gian thực = 1 năm trong game. 
* Một ngày thực tế trôi qua (24 giờ), tu sĩ sẽ già đi 24 tuổi trong game.
* Giao diện game luôn hiển thị một đồng hồ cát thọ nguyên: `Thọ nguyên còn lại: 45 năm / 150 năm`.

### 4.3. Cơ chế Luân Hồi Chuyển Thế (Reincarnation)
Khi người chơi **Chết già** hoặc **Thân tử đạo tiêu do lôi kiếp**:
* Nhân vật cũ biến mất khỏi bảng xếp hạng hiện tại.
* Người chơi được luân hồi đầu thai thành một tu sĩ mới thế hệ sau.
* **Di sản giữ lại (Chân Linh Điểm):** Dựa trên cảnh giới cao nhất kiếp trước đạt được, người chơi nhận được một lượng **Chân Linh Điểm** dùng để:
  * Nâng cấp phẩm chất Linh Căn (ví dụ: Từ Linh căn tạp phẩm $\rightarrow$ Song linh căn $\rightarrow$ Thiên linh căn tuyệt phẩm).
  * Giữ lại 1 cuốn công pháp cao cấp đã học.
  * Tốc độ tu luyện ở kiếp sau tăng vĩnh viễn $+10\%$ mỗi cấp Chân Linh.

---

## 5. HOẠT ĐỘNG TĂNG TU VI & PHÁT TRIỂN GAME

Để duy trì vòng lặp hấp dẫn, game cung cấp cả cơ chế thụ động (Idle) và chủ động (Active) để tích lũy tu vi và tài nguyên:

```
                            [ CÁC HOẠT ĐỘNG TĂNG TU VI ]
                                         |
         +-------------------------------+-------------------------------+
         |                               |                               |
    [ IDLE/PASSIVE ]              [ ACTIVE/GAMEPLAY ]             [ PVP & CO-OP ]
- Tĩnh Tọa Hấp Thu           - Động Phủ Cá Nhân              - Tranh Đoạt Linh Mạch
- Tụ Linh Trận (Động phủ)    - Du Ngoạn Kỳ Ngộ (Lựa chọn)    - PK cướp tài nguyên
- Offline income (Tối đa 8h) - Luyện Đan & Luyện Khí Các     - Tông Môn Chiến
```

### 5.1. Tĩnh Tọa Hấp Thu (Cultivate - Idle)
* **Mô tả:** Người chơi chỉ cần bấm nút "Tĩnh Tọa" để nhân vật bắt đầu tự động hấp thu linh khí thiên địa để chuyển hóa thành Tu Vi mỗi giây.
* **Công thức tăng trưởng thụ động:**
  $$\text{Tu Vi / Giây} = \text{Linh Khí Cơ Bản (Mạt Pháp = 1)} \times (1 + \text{Bonus Công Pháp} + \text{Bonus Cảnh Giới Tụ Linh Trận} + \text{Thiên Phú Hệ})$$
* **Tụ Linh Trận:** Đặt tại Động Phủ. Cấp độ trận pháp càng cao, phạm vi gom góp linh khí cạn kiệt càng lớn, tăng mạnh tốc độ tu luyện offline (tối đa tích lũy 8 giờ khi rời mạng).

### 5.2. Động Phủ Phân Tầng (Abode - Active & Social)
Động phủ của tu sĩ được quy hoạch chung tại **Thông Thiên Tháp Động Phủ** để chia sẻ linh mạch cốt lõi thời Mạt Pháp.
* **Cấu trúc phân tầng**: Tháp gồm nhiều tầng, mỗi tầng giới hạn tối đa **100 ô động phủ**. Tu sĩ phải bỏ Linh Thạch để thuê/mua đứt 1 ô đất tại tầng hiện tại để bắt đầu tu hành. Tầng càng cao thì linh khí buff tăng tu vi càng lớn (+10% mỗi tầng).
* **Quy tắc di chuyển**: Muốn lên tầng cao hơn thì tầng đó phải còn ô trống (< 100) và tu sĩ phải trả đủ phí mua ô mới (ô cũ được giải phóng hoàn trả 50% Linh thạch).
* **Phân khu chức năng**: Khi sở hữu ô đất thành công, người chơi được phát các phân khu sản xuất cá nhân:
  1. **🌱 Linh Điền (Đạo Tu tối ưu):** Trồng linh dược, thảo dược thô. Đạo Tu có thể bón phân rút ngắn thời gian để chế tạo đan dược tăng tu vi.
  2. **🐺 Yêu Vực (Nuôi thú - Ma Tu tối ưu):** Xây chuồng nuôi dưỡng yêu thú non (bắt được từ săn bắn), cho ăn thảo dược/khoáng thạch để lấy nguyên liệu hoặc thuần hóa thú trợ chiến (Pet).
  *(Lưu ý: Mỏ khai khoáng Linh Mạch quy định là tài nguyên dùng chung ngoài bản đồ thế giới, không nằm trong Động Phủ).*

### 5.3. Du Ngoạn Kỳ Ngộ (Text-based Adventure - Active)
Mỗi ngày người chơi có 5 lượt "Xuất Sơn" để du ngoạn giang hồ. Mỗi lần đi sẽ kích hoạt một sự kiện ngẫu nhiên hiển thị bằng văn bản và đi kèm các lựa chọn:

> **[Sự kiện Kỳ Ngộ: Vực sâu tàn cốt]**
> *Bạn đang đi dạo trên vách núi Thanh Vân thì vô tình trượt chân ngã xuống một hang động bí ẩn chứa một bộ xương khô của tu sĩ cổ đại. Trên tay bộ xương cầm một bình đan dược cổ.*
> * **Lựa chọn A: Quỳ lạy 3 cái rồi thành kính lấy bình đan.**
>   * *Kết quả:* 70% nhận được cổ đan phương *Trúc Cơ Đan* cực phẩm; 30% bị tàn hồn của tu sĩ đoạt xá (bị thương giảm 10% tu vi).
> * **Lựa chọn B: Lục lọi bộ xương ngay lập tức để tìm kho báu.**
>   * *Kết quả:* Tìm thấy 200 Linh thạch nhưng kích hoạt bẫy độc độc linh khí (giảm tốc độ tu luyện 20% trong 1 giờ).
> * **Lựa chọn C: Đốt xác tiêu hủy vì sợ tà ma ngoại đạo.**
>   * *Kết quả:* Nhận điểm Công Đức vĩnh viễn (+5% kháng lôi kiếp kiếp này).

### 5.4. Tranh Đoạt Linh Mạch Cực Phẩm (PVP - Resource Competition)
Vì thời đại Mạt Pháp chỉ sản sinh **1 triệu linh khí** mỗi ngày cho toàn bộ server:
* Hệ thống sẽ hiển thị danh sách các **Linh Mạch Cực Phẩm** (Mỏ tài nguyên chung).
* Người chơi có thể mang nhân vật của mình lên chiếm đóng mỏ.
* **Chiếm đóng thành công:** Tốc độ tăng tu vi của bạn sẽ được nhân 3 ($300\%$) trong thời gian giữ mỏ (Tối đa 4 giờ/ngày).
* **Cướp mỏ (PVP):** Người chơi khác có quyền thách đấu PK tự động để đẩy bạn ra khỏi mỏ. Trận đấu tính dựa trên Cảnh giới, Pháp bảo và Thần thông trang bị.

---

## 6. THIẾT KẾ GIAO DIỆN MÀN HÌNH DỌC (PORTRAIT UI)

Giao diện game thiết kế tối giản, gọn nhẹ dạng màn hình dọc (tỷ lệ 9:16), tối ưu cho mobile web.

### 6.1. Bố cục Layout Tổng quan

```
+-------------------------------------------------------------+
|  [AVATAR] Cảnh giới: TRÚC CƠ (Sơ Kỳ)     Linh thạch: 1,250 💎|
|  Thọ nguyên: 145/300 tuổi               Linh khí/s: +4.5/s  |
|  [====================== PROGRESS BAR TU VI (82%) =======]  |
+-------------------------------------------------------------+
|                                                             |
|                                                             |
|                     KHU VỰC HIỂN THỊ CHÍNH                  |
|                 (Thay đổi theo Tab đang chọn)               |
|                                                             |
|                                                             |
|                                                             |
+-------------------------------------------------------------+
|  [Hộp thoại log game: Bạn vừa trồng 1 gốc Tụ Linh Thảo...]  |
+-------------------------------------------------------------+
| [Tab Tu Luyện] [Tab Động Phủ] [Tab Giang Hồ] [Tab Túi] [Rank]|
+-------------------------------------------------------------+
```

### 6.2. Thiết Kế Chi Tiết các Tab Chức Năng

#### Tab 1: Tu Luyện (Cultivate)
* **Giao diện:** Trung tâm là hình ảnh vòng tròn bát quái thái cực tỏa sáng (hiệu ứng xoay nhẹ nhàng). 
* **Nút bấm lớn:** "Tĩnh Tọa Tu Luyện" (bật tắt tự động tăng tu vi) và "Đột Phá Cảnh Giới" (hiện lên khi thanh tiến trình đạt 100%).
* **Bảng Công Pháp đang vận hành:** Hiển thị công pháp đang trang bị (ví dụ: *Thanh Mộc Quyết* - tăng 1.5 linh khí/giây).

#### Tab 2: Động Phủ (Abode)
* **Giao diện:** 
  * Phía trên cùng hiển thị: `Thông Thiên Tháp Tầng: [X] - Vị trí ô: #[Y] (+X0% Linh khí/s)`. Kèm nút "Nâng Tầng" (mở danh sách 100 ô của tầng trên để xem/chọn mua).
  * Khu vực trung tâm hiển thị 3 phân khu chính:
    * **Linh Điền**: Grid 6 ô đất trồng trọt thảo dược thô và thời gian đếm ngược thu hoạch.
    * **Yêu Vực (Nuôi thú)**: Trạng thái 3 chuồng nuôi yêu thú, lượng thức ăn hiện có và thanh tiến trình trưởng thành của thú.
    * **Đan Phòng / Luyện Các**: Lò luyện đan phương (chế đan dược tăng tu vi/kháng lôi kiếp) và rèn pháp bảo.

#### Tab 3: Giang Hồ (World)
* **Giao diện:** Bản đồ các vùng đất mạt pháp phân chia theo cấp độ (Thanh Vân Thôn, Vạn Thú Sâm Lâm, Thiên Ma Cốc, Tiên Cổ Phế Tích).
* **Nút bấm:** "Ngao Du Giang Hồ" (tiêu hao 1 điểm Du ngoạn, hiển thị text sự kiện Kỳ Ngộ ngẫu nhiên).
* **Bí Cảnh Phong Ấn:** Các ải PVE leo tháp kiếm đan phương và công pháp thất truyền.

#### Tab 4: Túi Đồ (Inventory)
* **Giao diện:** Grid vật phẩm chia làm các tab con:
  * **Đan Dược:** *Tụ Khí Đan*, *Trúc Cơ Đan*, *Tẩy Tủy Đan*.
  * **Pháp Bảo:** *Khiên Tỷ Lôi*, *Kiếm Phi Kiếm*.
  * **Nguyên Liệu:** Khoáng thạch, linh dược thô, yêu đan thú.
  * **Công Pháp:** Các sách kỹ năng chưa học hoặc tàn quyển cổ tịch.

#### Tab 5: Bảng Xếp Hạng (Rankings)
* **Giao diện:** Danh sách Top 50 tu sĩ mạnh nhất server xếp hạng theo Tu Vi và Top Kỳ Ngộ Tuần.
* **Tông Môn:** Nơi thành lập hoặc tham gia Tông môn để nhận phúc lợi/tài nguyên chung.

### 6.3. Phong Cách Thiết Kế (UI/UX Aesthetics)
* **Chủ đạo:** Sleek Dark Mode (Nền đen sẫm `#0d0f12`, kết hợp màu xám tối `#1a1d24`).
* **Màu sắc điểm nhấn:**
  * **Đạo Tu:** Màu xanh lục ngọc `#00e676` và vàng kim hoàng đạo `#ffd600`.
  * **Thể Tu:** Màu đỏ cam máu `#ff3d00` và xám thép `#b0bec5`.
  * **Ma Tu:** Màu tím ma mị `#d500f9` và đỏ thẫm `#c62828`.
* **Hiệu ứng động (Micro-animations):**
  * Hiệu ứng luồng khí chạy dọc theo viền màn hình (linh khí triều tịch).
  * Vòng tròn lôi kiếp tích tụ sấm sét màu xanh lam khi chuẩn bị Đột phá cảnh giới.
  * Nút bấm sử dụng hiệu ứng Glassmorphism (nền mờ đục trong suốt, viền bóng).

### 6.4. Mục Tiêu UI Frontend MVP

Frontend cần ưu tiên cảm giác **đang tu hành liên tục**: người chơi mở game lên phải thấy ngay cảnh giới, tu vi, thọ nguyên, tốc độ hấp thu và hành động quan trọng tiếp theo. UI không làm theo kiểu landing page; màn hình đầu tiên sau đăng nhập là giao diện chơi thật.

* **Mobile-first portrait:** chiều rộng game tối đa `450px`, tỷ lệ trải nghiệm chính 9:16, desktop chỉ đóng vai trò khung bao thiết bị.
* **Thông tin quan trọng luôn hiện:** cảnh giới, tu vi, thọ nguyên, linh thạch, linh khí/giây, trạng thái socket.
* **Hành động chính rõ ràng:** Tĩnh tọa, Đột phá, Thu hoạch, Xuất sơn, Chiếm mỏ, Dùng vật phẩm.
* **Feedback tức thì:** mọi thao tác socket phải có trạng thái `pending`, thành công/thất bại, log sự kiện và hiệu ứng nhẹ.
* **Không quá nhiều chữ hướng dẫn:** text trong UI dùng để mô tả trạng thái game, vật phẩm, lựa chọn và kết quả; không dùng các đoạn giải thích cách dùng app dài dòng.

### 6.5. Khung Ứng Dụng FE

```
[AppShell]
  ├─ [PhoneFrame]              // khung obsidian trên desktop
  ├─ [ConnectionBanner]        // mất kết nối, reconnect, offline reward
  ├─ [PlayerStatusHeader]      // avatar, cảnh giới, tài nguyên, thọ nguyên
  ├─ [CultivationProgress]     // thanh tu vi + tốc độ tu luyện
  ├─ [MainViewport]
  │    ├─ CultivationView
  │    ├─ AbodeView
  │    ├─ WorldView
  │    ├─ InventoryView
  │    └─ RankingView
  ├─ [EventLogDrawer]          // log game dạng thu gọn/mở rộng
  └─ [BottomNavigation]        // 5 tab chính
```

**Nguyên tắc bố cục:**
* `PlayerStatusHeader` cố định ở đầu vùng game, không chiếm quá nhiều chiều cao để tránh đẩy nội dung chính xuống dưới.
* `MainViewport` là vùng cuộn chính; mỗi tab tự quản lý scroll nội bộ nếu có danh sách dài.
* `BottomNavigation` cố định đáy, dùng icon + label ngắn, có trạng thái active rõ ràng.
* `EventLogDrawer` mặc định hiển thị 1 dòng log mới nhất; người chơi có thể mở rộng để xem lịch sử.

### 6.6. Design Tokens Dành Cho React/Tailwind

| Token | Giá trị đề xuất | Dùng cho |
| :--- | :--- | :--- |
| `--color-bg-root` | `#020617` | nền ngoài cùng |
| `--color-bg-panel` | `rgba(15, 23, 42, 0.72)` | panel glass |
| `--color-border-soft` | `rgba(255, 255, 255, 0.06)` | viền panel |
| `--color-gold` | `#f59e0b` | CTA chính, linh thạch |
| `--color-jade` | `#10b981` | Đạo Tu, linh dược |
| `--color-fire` | `#f97316` | Thể Tu, lôi kiếp, cảnh báo |
| `--color-demon` | `#d946ef` | Ma Tu, yêu đan |
| `--radius-card` | `8px` | card vật phẩm/panel nhỏ |
| `--radius-control` | `8px` | button/input/tab |
| `--space-screen` | `16px` | padding màn hình |

**Quy tắc màu:** Không để toàn bộ giao diện bị một màu tím/xanh/amber thống trị. Nền tối là lớp chính, vàng kim chỉ dùng cho CTA và tài nguyên quý, jade/fire/demon dùng theo hệ tu hoặc loại nội dung.

### 6.7. Component UI Cốt Lõi

#### PlayerStatusHeader
Hiển thị tóm tắt nhân vật trong 2 tầng thông tin:
* Tầng 1: avatar nhỏ, tên, cảnh giới hiện tại, linh căn, trạng thái tu luyện.
* Tầng 2: linh thạch, thọ nguyên còn lại, linh khí/giây, Chân Linh Điểm nếu đang ở màn luân hồi.

Trạng thái nguy hiểm:
* Thọ nguyên còn dưới 20%: thanh thọ nguyên chuyển `fire`, thêm nhịp sáng nhẹ.
* Đủ điều kiện đột phá: hiển thị badge `Có thể đột phá`.
* Đang trọng thương: hiển thị debuff cùng thời gian còn lại.

#### CultivationProgress
* Thanh tiến trình tu vi có nhãn `currentExp / requiredExp`.
* Có chỉ báo `+x/s` và bonus đang tác động: công pháp, linh căn, tầng động phủ, linh mạch.
* Khi socket trả về cập nhật tu vi, thanh tăng mượt trong `300ms` để tạo cảm giác dòng linh khí đang vận hành.

#### PrimaryActionButton
Button chính dùng cho các hành động lớn:
* `Tĩnh Tọa Tu Luyện`
* `Đột Phá Cảnh Giới`
* `Thu Hoạch`
* `Ngao Du Giang Hồ`
* `Chiếm Đóng`

Button phải có icon phù hợp, trạng thái `loading`, `disabled`, `success`, `danger`. Không dùng text dài khiến vỡ layout trên mobile.

#### ResourcePill
Chip nhỏ hiển thị tài nguyên: Linh thạch, Linh dược, Khoáng thạch, Yêu đan, lượt du ngoạn. Mỗi pill có icon, số lượng rút gọn (`1.2K`, `3.4M`) và tooltip/chi tiết khi chạm giữ hoặc mở modal.

#### EventLog
Log là một phần gameplay, không chỉ là debug:
* Log thường: màu slate, ví dụ `Bạn hấp thu 12 tu vi.`
* Log nhận thưởng: màu jade/gold.
* Log cảnh báo: màu fire.
* Log nguy hiểm/PK/thiên kiếp: màu demon hoặc fire, có rung nhẹ một lần.

### 6.8. Thiết Kế Theo Màn Hình

#### 6.8.1. Auth & Chọn Đạo Lộ
* Màn hình đăng nhập/đăng ký đặt trong khung portrait, nền có ảnh/texture tiên hiệp tối, không dùng layout marketing.
* Form chỉ gồm trường cần thiết. Input có icon phải dùng padding trái tối thiểu `2.75rem`.
* Sau khi tạo nhân vật, màn chọn đạo lộ hiển thị 3 lựa chọn: Đạo Tu, Thể Tu, Ma Tu. Mỗi lựa chọn có màu, thiên phú, vòng lặp phát triển và nút xác nhận.

#### 6.8.2. Tu Luyện View
Mục tiêu: người chơi nhìn thấy tiến trình tăng tu vi và quyết định có nên đột phá hay chuẩn bị thêm.

Thành phần:
* Vòng bát quái ở giữa, có trạng thái `idle`, `cultivating`, `breakthrough-ready`, `tribulation`.
* Bảng bonus tu luyện gồm công pháp, linh căn, động phủ, linh mạch.
* CTA `Tĩnh Tọa` bật/tắt trạng thái hấp thu.
* CTA `Đột Phá` chỉ nổi bật khi đủ tu vi; trước khi bấm mở modal xác nhận lôi kiếp.

Modal Đột Phá:
* Hiển thị tỷ lệ thành công cuối cùng, buff từ đan dược/pháp bảo/trận pháp.
* Hiển thị rủi ro: trọng thương, tử vong/luân hồi.
* Cho phép chọn vật phẩm hỗ trợ trước khi gửi socket.

#### 6.8.3. Động Phủ View
Mục tiêu: quản lý tài sản cá nhân trong Thông Thiên Tháp, sản xuất tài nguyên và nâng tầng.

Thành phần:
* Header tầng: `Tầng X`, `Ô #Y`, bonus linh khí, độ kín tầng `n/100`.
* Nút `Nâng Tầng` mở modal danh sách tầng kế tiếp, giá mua, số ô còn trống, điều kiện cảnh giới.
* Segment control: `Linh Điền`, `Yêu Vực`, `Đan/Luyện`.
* Linh Điền: grid 6 ô, mỗi ô có trạng thái `empty`, `growing`, `ready`, `diseased`.
* Yêu Vực: 3 chuồng, thanh trưởng thành, thức ăn, lựa chọn thu hoạch nguyên liệu hoặc thuần hóa pet.
* Đan/Luyện: hàng đợi chế tạo, nguyên liệu thiếu, tỷ lệ thành công.

#### 6.8.4. Giang Hồ View
Mục tiêu: đưa người chơi ra ngoài vòng idle bằng kỳ ngộ, bí cảnh và tranh đoạt tài nguyên.

Thành phần:
* Bản đồ vùng dạng danh sách có cấp độ, tài nguyên chính, độ nguy hiểm.
* Counter lượt `Xuất Sơn` trong ngày.
* Kỳ ngộ hiển thị như một đoạn truyện ngắn kèm 2-3 lựa chọn rõ ràng.
* Khu Linh Mạch dùng chung hiển thị các node: phẩm cấp, chủ sở hữu, thời gian giữ còn lại, bonus, nút `Chiếm` hoặc `Thách Đấu`.

#### 6.8.5. Túi Đồ View
Mục tiêu: giúp người chơi tìm và dùng vật phẩm nhanh.

Thành phần:
* Tabs con: `Đan`, `Pháp Bảo`, `Nguyên Liệu`, `Công Pháp`, `Pet`.
* Grid item ổn định kích thước, không nhảy layout khi số lượng thay đổi.
* Màu phẩm cấp theo `frontend-rules.md`: thường, huyền phẩm, linh bảo, trân phẩm, cực phẩm.
* Item detail bottom sheet: mô tả, số lượng, hiệu ứng, hành động `Dùng`, `Trang Bị`, `Học`, `Khóa`.

#### 6.8.6. Bảng Xếp Hạng View
Mục tiêu: tạo áp lực cạnh tranh nhưng đọc nhanh.

Thành phần:
* Tabs `Tu Vi`, `Kỳ Ngộ Tuần`, `Linh Mạch`, `Tông Môn`.
* Top 3 có treatment nổi bật nhưng không chiếm quá nhiều chiều cao.
* Hàng của người chơi luôn được ghim hoặc hiển thị ở cuối danh sách nếu không nằm trong top.
* Mỗi dòng có tên, cảnh giới, hệ tu, điểm xếp hạng, biến động thứ hạng nếu có.

### 6.9. State, Socket Và Loading UX

Frontend dùng Zustand để tách state theo domain:

```
useAuthStore
usePlayerStore
useCultivationStore
useAbodeStore
useWorldStore
useInventoryStore
useRankingStore
useEventLogStore
useSocketStore
```

**Nguyên tắc cập nhật socket:**
* Mỗi action gửi WebSocket phải tạo `requestId` cục bộ để khóa nút liên quan, tránh spam thao tác.
* Khi nhận response thành công, cập nhật store tương ứng và ghi log game.
* Khi lỗi, giữ nguyên dữ liệu cũ, mở toast/bottom sheet lỗi ngắn và ghi log cảnh báo.
* Khi mất kết nối, UI chuyển sang trạng thái đọc được nhưng khóa các action ghi dữ liệu.
* Khi reconnect, gọi request đồng bộ trạng thái nhân vật, túi đồ, động phủ và bảng log mới nhất.

**Loading skeleton:**
* Header dùng skeleton 2 dòng.
* Grid Linh Điền/Túi Đồ dùng placeholder giữ nguyên kích thước ô.
* Ranking dùng skeleton list 8 dòng.

### 6.10. Quy Tắc Responsive & Accessibility

* Hit target tối thiểu `44px` cho button, tab, item có tương tác.
* Không dùng font scale theo viewport width; dùng size cố định theo cấp bậc typography.
* Text dài trong item phải xuống dòng tối đa 2 dòng hoặc mở chi tiết trong bottom sheet.
* Tương phản chữ/nền phải đủ rõ trên màn hình mobile sáng ngoài trời.
* Animation có thể tắt qua `prefers-reduced-motion`.
* Modal/bottom sheet phải focus đúng nút hành động chính và đóng được bằng ESC trên desktop.

### 6.11. Checklist Build FE Theo Giai Đoạn

#### Giai đoạn 1: Playable Shell
* App shell portrait + phone frame desktop.
* Auth, chọn đạo lộ, header trạng thái nhân vật.
* Bottom navigation 5 tab.
* Socket connect/reconnect banner.

#### Giai đoạn 2: Core Loop Tu Luyện
* Tu Luyện View, progress tu vi realtime, tĩnh tọa.
* Modal đột phá, hiển thị tỷ lệ và rủi ro.
* Event log gameplay.

#### Giai đoạn 3: Sản Xuất Động Phủ
* Động Phủ View, tầng/ô đất, nâng tầng.
* Linh Điền 6 ô, Yêu Vực 3 chuồng, Đan/Luyện.
* Inventory item detail và hành động dùng/trang bị.

#### Giai đoạn 4: Cạnh Tranh & Retention
* Giang Hồ kỳ ngộ.
* Linh Mạch PVP resource nodes.
* Ranking realtime.
* Offline reward và luân hồi flow.

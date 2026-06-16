# TỔNG QUAN DỰ ÁN (PROJECT OVERVIEW) - DỰ ÁN PHÀM NHÂN

Dự án **Phàm Nhân** (`phamnhan`) là một hệ thống game backend / mô phỏng thế giới tu tiên (Cultivation/Xianxia game server). Hệ thống cho phép người chơi thực hiện các hoạt động như tu luyện (tăng tu vi), tham gia kỳ ngộ (encounters), thám hiểm phụ bản (dungeons), săn lùng bản đồ kho báu (treasure maps) và nhận thưởng hàng tuần.

---

## 1. MỤC TIÊU DỰ ÁN
* **Xây dựng game server hiệu năng cao**: Xử lý mượt mà các logic tính toán tu vi, phần thưởng, tỷ lệ rơi vật phẩm và tương tác giữa các người chơi.
* **Hệ thống bền vững & dễ mở rộng**: Kiến trúc module hóa giúp dễ dàng thêm phụ bản, vật phẩm, hoạt động mới mà không ảnh hưởng tới logic cốt lõi.
* **Công bằng và bảo mật**: Chống gian lận trong việc tính toán tu vi và phần thưởng.

---

## 2. CÁC TÍNH NĂNG CHÍNH (CORE FEATURES)
* **Hệ thống Tu Vi & Cảnh Giới**: Người chơi tu luyện tích lũy tu vi để đột phá các cảnh giới (Luyện Khí, Trúc Cơ, Kết Đan, Nguyên Anh, v.v.).
* **Kỳ Ngộ Tuần (Weekly Encounters)**: Các sự kiện ngẫu nhiên xảy ra với người chơi hàng tuần, xếp hạng dựa trên số lượng kỳ ngộ và trao thưởng vào cuối tuần.
* **Phụ Bản & Săn Báu (Dungeons & Treasure Maps)**: Người chơi vượt phụ bản để nhận nguyên liệu, trang bị và bản đồ kho báu với tỷ lệ rơi (drop rate) được kiểm soát nghiêm ngặt.
* **Bảng Xếp Hạng & Trao Thưởng**: Xếp hạng tu vi, kỳ ngộ tuần và tự động phát thưởng thông qua hệ thống thư (mail system) hoặc cộng trực tiếp tài nguyên.

---

## 3. THUẬT NGỮ TRONG GAME (DOMAIN TERMS)
* **Tu Vi (Cultivation)**: Điểm kinh nghiệm tích lũy để tăng cấp cảnh giới.
* **Kỳ Ngộ (Encounter)**: Sự kiện ngẫu nhiên mang lại cơ duyên (vật phẩm, tu vi hoặc thử thách).
* **Phụ Bản (Dungeon)**: Các ải thử thách mà người chơi cần vượt qua để nhận thưởng.
* **Bản Đồ Kho Báu (Treasure Map)**: Vật phẩm đặc biệt mở ra các khu vực ẩn chứa phần thưởng giá trị lớn.
* **Đột Phá (Breakthrough)**: Quá trình thăng cấp từ cảnh giới này sang cảnh giới khác, có thể có tỷ lệ thất bại.

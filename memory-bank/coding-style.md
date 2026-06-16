# QUY TẮC VIẾT CODE (CODING STYLE GUIDE)

Tài liệu này định nghĩa các tiêu chuẩn viết code bắt buộc áp dụng trong toàn bộ dự án **Phàm Nhân** để đảm bảo tính đồng nhất, dễ đọc và dễ bảo trì.

---

## 1. QUY TẮC ĐẶT TÊN (NAMING CONVENTIONS)
* **Thư mục & Tệp tin**: Sử dụng `kebab-case` cho thư mục (ví dụ: `memory-bank`) và `camelCase` hoặc `kebab-case` cho tệp code (ví dụ: `dungeonService.js` hoặc `dungeon-service.js`). Ưu tiên tính đồng bộ với các tệp hiện tại.
* **Biến & Hàm**: Sử dụng `camelCase`. Tên phải rõ nghĩa, thể hiện hành động hoặc trạng thái.
  * *Tốt*: `calculateTuViBonus()`, `isBreakthroughSuccessful`, `dungeonDropRate`.
  * *Không tốt*: `calc()`, `check()`, `flag`, `tv`.
* **Hằng số (Constants)**: Sử dụng `UPPER_SNAKE_CASE`. Tất cả các tỷ lệ phần trăm, giới hạn, cấu hình trò chơi phải đặt trong hằng số.
  * *Ví dụ*: `DEFAULT_TREASURE_MAP_DROP_CHANCE = 0.05;` (5%).
* **Class & Model**: Sử dụng `PascalCase`.
  * *Ví dụ*: `UserModel`, `DungeonController`.

---

## 2. CÚ PHÁP & PHONG CÁCH VIẾT (SYNTAX & PATTERNS)
* **Xử lý bất đồng bộ (Asynchronous)**: Luôn ưu tiên dùng `async/await` thay vì `.then().catch()` hoặc callbacks truyền thống.
* **Xử lý Lỗi (Error Handling)**:
  * Không bao giờ nuốt lỗi (empty catch). Ít nhất phải log lỗi thông qua hệ thống Logger.
  * Luôn kiểm tra điều kiện biên (edge cases) và trả về lỗi sớm (Early Return Pattern).
  * Ví dụ mẫu:
    ```javascript
    async function performBreakthrough(userId) {
      const user = await userRepository.findById(userId);
      if (!user) {
        throw new Error("Người chơi không tồn tại.");
      }

      if (user.tuVi < user.requiredTuViForBreakthrough) {
        throw new Error("Chưa tích lũy đủ tu vi để đột phá.");
      }

      // Logic đột phá...
    }
    ```

---

## 3. TRÁNH DÙNG SỐ MA THUẬT (NO MAGIC NUMBERS)
Tất cả các số liệu cấu hình game (như tỷ lệ rơi bản đồ kho báu là `0.05`, tu vi cần thiết, sát thương phụ bản) **không được** viết trực tiếp vào dòng logic xử lý. Hãy đưa chúng vào một file cấu hình hoặc hằng số.
* *Sai*: `if (Math.random() < 0.05) { dropTreasureMap(); }`
* *Đúng*:
  ```javascript
  const { TREASURE_MAP_DROP_CHANCE } = require('../constants/dropRates');
  // ...
  if (Math.random() < TREASURE_MAP_DROP_CHANCE) {
      dropTreasureMap();
  }
  ```

---

## 4. CHÚ THÍCH (COMMENTS)
* Viết JSDoc cho các hàm quan trọng để AI và Linter có thể hiểu kiểu dữ liệu đầu vào/đầu ra.
* Giải thích rõ lý do "Tại sao" làm thế này thay vì giải thích "Làm thế nào" (trừ khi thuật toán quá phức tạp).
* Giữ lại các chú thích hiện có khi cập nhật hoặc sửa đổi code.

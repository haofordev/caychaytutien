# QUYẾT ĐỊNH KỸ THUẬT (ARCHITECTURAL DECISIONS)

Tài liệu này lưu trữ dưới dạng **Architectural Decision Records (ADR)**. Khi hệ thống có các thay đổi lớn về công nghệ hoặc kiến trúc, hãy viết thêm một ADR mới vào đây.

---

## [ADR-001] SỬ DỤNG REDIS SORTED SET CHO HỆ THỐNG BẢNG XẾP HẠNG (LEADERBOARD)

### Trạng thái
**ĐÃ DUYỆT (ACCEPTED)**

### Ngữ cảnh (Context)
Game có số lượng người chơi lớn, nhu cầu xem bảng xếp hạng tu vi và bảng xếp hạng kỳ ngộ tuần của người chơi rất cao và liên tục. Nếu thực hiện câu lệnh `find().sort({ tuVi: -1 }).limit(10)` trực tiếp trên database MongoDB mỗi lần người chơi mở bảng xếp hạng, server sẽ bị nghẽn I/O khi lượng CCU (Concurrent Users) tăng cao.

### Quyết định (Decision)
* Sử dụng **Redis Sorted Set (ZSET)** để lưu trữ và quản lý bảng xếp hạng thời gian thực.
* Mỗi khi người chơi nhận tu vi hoặc hoàn thành kỳ ngộ, ứng dụng sẽ gọi `ZADD` hoặc `ZINCRBY` lên Redis.
* Khi người chơi truy vấn bảng xếp hạng, API sẽ đọc trực tiếp từ Redis bằng lệnh `ZREVRANGE`.
* Database MongoDB vẫn lưu trữ tu vi gốc của người chơi làm bản backup chính xác nhất.

### Hệ quả (Consequences)
* **Tích cực**:
  * Tốc độ truy vấn bảng xếp hạng cực nhanh (độ phức tạp O(log(N) + M), phản hồi dưới 5ms).
  * Giảm tải hoàn toàn cho MongoDB.
* **Tiêu cực**:
  * Phải đảm bảo tính đồng bộ dữ liệu giữa MongoDB và Redis. Nếu Redis gặp sự cố, cần có cơ chế khôi phục (rebuild) lại ZSET từ MongoDB.

---

## [ADR-002] TÍNH TOÁN TỶ LỆ RƠI ĐỒ BẰNG PHÂN SỐ VẠN (BASIS POINTS - BPS)

### Trạng thái
**ĐÃ DUYỆT (ACCEPTED)**

### Ngữ cảnh (Context)
Việc sử dụng số thực float (ví dụ: `0.05` cho 5%, `0.001` cho 0.1% map kho báu) trong Javascript dễ dẫn đến sai số làm tròn khi thực hiện các phép tính nhân tỷ lệ buff may mắn (ví dụ: tăng 15% của tỷ lệ 0.1%).

### Quyết định (Decision)
* Quy chuẩn tỷ lệ trong code sử dụng số nguyên với đơn vị **phần vạn** (Basis Points - BPS).
* Quy ước quy đổi:
  * `100%` = `10,000 BPS`
  * `10%` = `1,000 BPS`
  * `1%` = `100 BPS`
  * `0.1%` = `10 BPS`
* Mọi phép tính nhân/chia may mắn sẽ thực hiện bằng số nguyên và chia cho `10,000` ở bước cuối cùng trước khi so sánh.

### Hệ quả (Consequences)
* **Tích cực**:
  * Loại bỏ hoàn toàn lỗi làm tròn số thập phân của Javascript.
  * Việc cấu hình tỷ lệ rơi trong database/config trở nên tường minh, an toàn, dễ đọc dưới dạng số nguyên.
* **Tiêu cực**:
  * Lập trình viên và AI cần làm quen với việc chuyển đổi từ phần trăm sang BPS khi cấu hình game.

---

## [ADR-003] THIẾT KẾ CƠ CHẾ TIẾN TRÌNH TU TIÊN: THỌ NGUYÊN, LUÂN HỒI VÀ THIÊN KIẾP LÔI ĐÌNH

### Trạng thái
**ĐÃ DUYỆT (ACCEPTED)**

### Ngữ cảnh (Context)
Cốt truyện của game là thời kỳ Mạt Pháp linh khí suy kiệt (chỉ còn 1%). Để tạo áp lực sinh tồn, tính cạnh tranh cao và động lực phát triển vòng lặp gameplay (gameplay loop), game cần có cơ chế ràng buộc về thời gian tu luyện và rủi ro khi đột phá cảnh giới.

### Quyết định (Decision)
* **Hệ thống Thọ Nguyên (Lifespan)**: Mỗi cảnh giới có giới hạn thọ nguyên cụ thể (Phàm nhân 100 tuổi, Luyện Khí 150 tuổi, Trúc Cơ 300 tuổi, v.v.). Thời gian quy đổi: 1 giờ ngoài đời = 1 năm trong game. Nếu hết thọ nguyên mà không đột phá, nhân vật chết già.
* **Cơ chế Luân Hồi (Reincarnation)**: Khi chết già hoặc tử vong do lôi kiếp, người chơi chuyển kiếp đầu thai thành nhân vật mới. Nhận **Chân Linh Điểm** dựa trên cảnh giới kiếp trước để nâng cấp Linh Căn vĩnh viễn và mang theo một số di sản ở kiếp sau.
* **Thiên Kiếp Lôi Đình**: Việc thăng cấp cảnh giới lớn đi kèm tỷ lệ thất bại và rủi ro. Người chơi có thể sử dụng Đan Dược (như Trúc Cơ Đan), Pháp Bảo phòng ngự (Thể Tu rèn) hoặc Trận Pháp động phủ để hấp thu lôi kiếp và nâng cao tỷ lệ thành công.
* **Giao diện Màn hình Dọc (Portrait UI)**: Game được định dạng hiển thị dọc (tỷ lệ 9:16), điều hướng bằng 5 tab chính (Tu Luyện, Động Phủ, Giang Hồ, Túi Đồ, Bảng Xếp Hạng) để tối ưu hóa trải nghiệm trên mobile web.

### Hệ quả (Consequences)
* **Tích cực**:
  * Tăng tính chiều sâu chiến thuật: Người chơi phải cân đối thời gian giữa tích lũy tu vi, trồng dược luyện đan, khai khoáng rèn khí và săn quái.
  * Tăng tính giữ chân người chơi (Retention): Cơ chế Luân Hồi giúp người chơi có động lực tiếp tục chơi lại ở kiếp sau với buff tăng trưởng mạnh hơn.
* **Tiêu cực**:
  * Logic tính toán thời gian thọ nguyên và xử lý luân hồi phức tạp hơn ở phía backend.

---

## [ADR-004] SỬ DỤNG PROTOBUF CHO SOCKET NHỊ PHÂN VÀ PRISMA ORM VỚI POSTGRESQL

### Trạng thái
**ĐÃ DUYỆT (ACCEPTED)**

### Ngữ cảnh (Context)
Game yêu cầu truyền nhận dữ liệu thời gian thực (real-time) cho toàn bộ tính năng và cần tối ưu hóa băng thông truyền tải vì số lượng kết nối đồng thời (CCU) có thể rất lớn. Đồng thời, cấu trúc dữ liệu game có tính quan hệ chặt chẽ (giữa người chơi, túi đồ, kỳ ngộ, mỏ khoáng chiếm giữ) nên cần một ORM mạnh mẽ để quản lý các tác vụ truy vấn database quan hệ một cách tin cậy.

### Quyết định (Decision)
* **WebSocket Binary via Protobuf**:
  * Sử dụng định dạng nhị phân **Protocol Buffers (Protobuf)** để mã hóa/giải mã toàn bộ tin nhắn truyền tải qua WebSocket.
  * Cấu trúc gói tin nhị phân: 2 bytes đầu chứa mã hành động (Opcode), các bytes sau chứa payload đã mã hóa.
* **Prisma ORM & PostgreSQL**:
  * Chuyển đổi hệ quản trị cơ sở dữ liệu từ MongoDB sang **PostgreSQL** để hỗ trợ tốt các ràng buộc khóa ngoại và toàn vẹn dữ liệu.
  * Sử dụng **Prisma ORM** để quản lý database schema, tự động tạo migrations và truy vấn dữ liệu hiệu năng cao.
* **Đóng gói Docker**:
  * Triển khai môi trường Production bằng **Docker** và **Docker Compose**, sử dụng multi-stage build để thu nhỏ kích thước container của React Frontend và Express Backend.

### Hệ quả (Consequences)
* **Tích cực**:
  * Tiết kiệm tới 70-80% băng thông truyền tải gói tin socket so với việc gửi định dạng JSON truyền thống.
  * Đảm bảo đồng bộ schema dữ liệu chặt chẽ giữa FE và BE thông qua tệp tin `.proto` chung.
  * Prisma ORM giúp loại bỏ rủi ro sai sót truy vấn SQL thủ công và hỗ trợ migration cơ sở dữ liệu một cách an toàn, có hệ thống.
  * Việc đóng gói Docker giúp triển khai (deployment) lên các môi trường production nhanh chóng, nhất quán.
* **Tiêu cực**:
  * Quy trình phát triển phức tạp hơn do phải chạy lệnh biên dịch/load tệp `.proto` khi thay đổi cấu trúc dữ liệu.
  * Phải quản lý việc phân tích (parse) nhị phân tại cả Client (React) và Server (Node.js).

---

## [ADR-005] THIẾT KẾ HỆ THỐNG THÔNG THIÊN ĐỘNG PHỦ (PHÂN TẦNG XÃ HỘI)

### Trạng thái
**ĐÃ DUYỆT (ACCEPTED)**

### Ngữ cảnh (Context)
Trong thời đại Mạt Pháp linh khí cạn kiệt, việc mỗi người chơi sở hữu một động phủ cá nhân biệt lập không phản ánh đúng tính sinh tồn và khan hiếm tài nguyên. Đồng thời, game cần các cơ chế xã hội kích thích giao dịch, cạnh tranh gián tiếp và tạo mục tiêu phấn đấu trung hạn (kiếm tiền mua bất động sản tốt hơn).

### Quyết định (Decision)
* **Quy hoạch tập trung**: Toàn bộ động phủ của máy chủ được quy hoạch chung tại **Thông Thiên Tháp Động Phủ**.
* **Giới hạn 100 ô/tầng**: Mỗi tầng tháp chỉ chứa tối đa 100 ô đất (plotIndex 1 -> 100). Khi một tầng đầy 100/100, người chơi khác không thể di chuyển lên tầng đó.
* **Cơ chế Thuê/Mua và Lên Tầng**:
  * Người chơi bỏ Linh Thạch mua đứt 1 ô đất tại tầng thích hợp (giá mua tăng gấp đôi sau mỗi tầng).
  * Lên tầng cao hơn tăng thêm **+10%** tốc độ tu luyện tĩnh tọa cơ bản trên mỗi tầng.
  * Khi nâng cấp lên tầng mới thành công, ô đất cũ ở tầng dưới sẽ tự động được thu hồi và hoàn trả **50%** giá trị mua ban đầu.
* **Mở khóa hoạt động sản xuất**: Sở hữu thành công ô đất sẽ phát hai khu vực sản xuất: **Linh Điền** (trồng linh thảo chế đan dược) và **Yêu Vực** (nuôi dưỡng thú non lấy nguyên liệu rèn đan/khí hoặc làm Pet trợ chiến).

### Hệ quả (Consequences)
* **Tích cực**:
  * Tạo tính cạnh tranh xã hội lành mạnh: Người chơi nỗ lực kiếm tiền và nâng cảnh giới để chiếm giữ các ô đất ở tầng cao trước khi chúng bị đầy.
  * Tạo luồng tiêu tốn (sink) Linh Thạch cực kỳ hiệu quả, giúp cân bằng nền kinh tế trong game.
  * Đồng bộ tốt với Prisma schema bằng ràng buộc Unique trên `[floor, plotIndex]`.
* **Tiêu cực**:
  * Cần xử lý đồng bộ trạng thái khi có người di chuyển tầng để giải phóng ô đất cũ ngay lập tức ở phía database.


---

## [ADR-006] CHUẨN HÓA UI FRONTEND THEO APP SHELL PORTRAIT CYBER-XIANXIA

### Trạng thái
**ĐÃ DUYỆT (ACCEPTED)**

### Ngữ cảnh (Context)
Game cần một hướng UI Frontend rõ ràng để chuyển từ tài liệu gameplay sang triển khai React/Tailwind. Trải nghiệm chính là mobile web màn hình dọc, nhưng vẫn phải đẹp trên desktop bằng khung thiết bị. Người chơi cần nhìn thấy ngay trạng thái tu luyện, tài nguyên và hành động tiếp theo mà không bị che bởi bố cục marketing hoặc hướng dẫn dài dòng.

### Quyết định (Decision)
* Dùng `AppShell` portrait làm khung chính cho toàn bộ frontend, gồm `PlayerStatusHeader`, `CultivationProgress`, `MainViewport`, `EventLogDrawer` và `BottomNavigation`.
* Giữ 5 tab gameplay chính: Tu Luyện, Động Phủ, Giang Hồ, Túi Đồ, Bảng Xếp Hạng.
* Chuẩn hóa các component cốt lõi: `PrimaryActionButton`, `ResourcePill`, `EventLog`, modal đột phá, item detail bottom sheet và các skeleton loading giữ layout ổn định.
* Frontend state tách theo domain bằng Zustand: auth, player, cultivation, abode, world, inventory, ranking, event log và socket.
* Mọi action socket phải có trạng thái pending/error/success, khóa thao tác liên quan trong lúc chờ response và ghi log game ngắn gọn.
* Design tokens và quy tắc responsive/accessibility được ghi trong `game-design.md` mục 6.4 đến 6.11, đồng bộ với `memory-bank/frontend-rules.md`.

### Hệ quả (Consequences)
* **Tích cực**:
  * FE có roadmap build rõ theo MVP: playable shell, core loop tu luyện, sản xuất động phủ, cạnh tranh/retention.
  * Component và state domain rõ ràng giúp dễ nối với WebSocket binary/Protobuf hiện có.
  * UI tập trung gameplay thật, giảm nguy cơ sa vào landing page hoặc giao diện chỉ để trình diễn.
* **Tiêu cực**:
  * Cần kiểm soát kỹ chiều cao header, log và bottom nav để không làm vùng chơi chính bị chật trên mobile nhỏ.
  * Các animation, glassmorphism và trạng thái socket cần được test trên thiết bị yếu để tránh giảm hiệu năng.

---

## [ADR-007] CHUẨN HÓA RULE CHO AI AGENT KHI TRIỂN KHAI FRONTEND

### Trạng thái
**ĐÃ DUYỆT (ACCEPTED)**

### Ngữ cảnh (Context)
Dự án có nhiều AI Agent và developer cùng có thể chỉnh Frontend. Nếu mỗi agent tự diễn giải UI/UX theo thói quen riêng, giao diện dễ lệch khỏi phong cách Cyber-Xianxia, phá layout portrait hoặc làm sai flow socket/Protobuf.

### Quyết định (Decision)
* Bổ sung rule bắt buộc cho AI trong `AGENTS.md` mục **5. Quy Tắc Bắt Buộc Khi Code Frontend**.
* Bổ sung checklist triển khai chi tiết trong `memory-bank/frontend-rules.md` mục **7. Quy Tắc Cho AI Khi Triển Khai Frontend**.
* Mọi AI khi code FE phải đọc `frontend-rules.md`, `game-design.md` mục 6, `architecture.md` và component/store hiện có trước khi sửa.
* FE phải bám AppShell portrait, Zustand domain state, WebSocket action states, skeleton loading và visual tokens đã chuẩn hóa.
* Cấm tự ý cài package, đổi Protobuf schema/opcode hoặc tạo landing page khi task là gameplay UI.

### Hệ quả (Consequences)
* **Tích cực**:
  * Giảm rủi ro AI tạo UI lệch phong cách hoặc phá layout mobile-first.
  * FE code dễ nhất quán hơn giữa các lần sửa bởi nhiều agent.
  * Các flow socket/loading/error được yêu cầu ngay từ rule, tránh build UI chỉ có trạng thái happy path.
* **Tiêu cực**:
  * Agent cần đọc nhiều tài liệu hơn trước khi code FE.
  * Các thay đổi UI thử nghiệm cần cập nhật rule nếu trở thành chuẩn mới.

---

## [ADR-008] THÊM HỆ THỐNG NGŨ HỆ LINH CĂN MỞ KHÓA THEO NHIỆM VỤ

### Trạng thái
**ĐÃ DUYỆT (ACCEPTED)**

### Ngữ cảnh (Context)
Flow tạo nhân vật cần cho người chơi một lựa chọn miễn phí đủ rõ ràng ngay khi vào game, nhưng vẫn cần mục tiêu phát triển dài hạn để họ tiếp tục mở rộng hướng build sau giai đoạn đầu. Linh Căn trước đây chủ yếu mô tả phẩm chất tăng tốc tu luyện, chưa tách rõ hệ ngũ hành và điều kiện mở thêm hệ.

### Quyết định (Decision)
* Tách Linh Căn thành **phẩm chất** và **hệ ngũ hành**.
* Sau Khảo Nghiệm Linh Căn, người chơi được chọn miễn phí 1 hệ khởi nguyên trong **Kim, Mộc, Thủy, Hỏa, Thổ**.
* Bốn hệ còn lại được mở bằng nhiệm vụ theo mốc cảnh giới, tài nguyên và hoạt động gameplay: kỳ ngộ, động phủ, bí cảnh ngũ hành, lôi kiếp và chuỗi Ngũ Khí Triều Nguyên.
* Mọi đạo lộ Đạo Tu, Thể Tu, Ma Tu đều có thể mở đủ 5 hệ, nhưng trong một thời điểm chỉ kích hoạt 1 hệ chủ tu và tối đa 2 hệ phụ tu để tránh cộng dồn bonus quá mạnh.

### Hệ quả (Consequences)
* **Tích cực**:
  * Flow nhập môn rõ hơn: đăng ký -> chọn đạo lộ -> chọn 1 hệ linh căn miễn phí -> vào game.
  * Tạo mục tiêu trung hạn/dài hạn thông qua mở khóa từng hệ thay vì chỉ tăng chỉ số tuyến tính.
  * Cho phép nhiều hướng build và combo công pháp mà không khóa cứng người chơi vào lựa chọn ban đầu.
* **Tiêu cực**:
  * Backend/Frontend cần lưu danh sách hệ đã mở, hệ chủ tu, hệ phụ tu và tiến độ nhiệm vụ mở khóa.
  * Cần cân bằng kỹ bonus combo để không làm một số hệ trở thành lựa chọn bắt buộc.

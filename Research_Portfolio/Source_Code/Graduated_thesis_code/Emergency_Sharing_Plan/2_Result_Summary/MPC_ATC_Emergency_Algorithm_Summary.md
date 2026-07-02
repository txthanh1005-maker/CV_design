# Tóm tắt Mô hình và Thuật toán: Decentralized Emergency Power Sharing using ATC-SOCP

Tài liệu này tổng hợp lại các thay đổi cốt lõi của mô hình toán học và thuật toán trong thư mục mã nguồn hiện tại (`Current_ATC_Model`) nhằm mục đích cung cấp tài liệu tham khảo cho việc đọc hiểu và viết Literature Review.

## 1. Bối cảnh Hệ thống (System Context)
Hệ thống chuyển đổi từ **Giao dịch Năng lượng ngang hàng (P2P Trading)** sang **Chia sẻ Công suất Khẩn cấp (Emergency Power Sharing)**.
Mô hình cấu trúc gồm 2 lớp (Two-layer architecture):
- **Lớp 1 (Local Level - SOCP):** Bài toán Tối ưu Hạt nhân của từng Microgrid (MG). Sử dụng ràng buộc luồng công suất nhánh (Branch Flow Model) kết hợp nới lỏng nón bậc hai (SOCP Relaxation) để đảm bảo các yếu tố vật lý của mạng điện.
- **Lớp 2 (Coordination Level - ATC):** Thuật toán phân cấp Analytical Target Cascading (ATC). System Operator (DSO) đóng vai trò trung tâm phân phối, cấp mục tiêu truyền tải (Tie-line Target) và điều phối để các MGs san sẻ công suất cho nhau khi có sự cố.

## 2. Mô hình Local SOCP (Lớp 1)

### Rút gọn biến và Tối thiểu hóa Cắt Tải (Load Shedding)
Trong trường hợp khẩn cấp (Islanded / Fault), mục tiêu hàng đầu của hệ thống không còn là tối đa hóa lợi nhuận mà là **tối thiểu hóa lượng điện năng bị cắt (Minimize Load Shedding)** để cứu lưới.
- Biến $P_{shed}$ đại diện cho công suất phụ tải bị sa thải tại từng nút.
- Hàm mục tiêu (khi kích hoạt cờ `stage='Emergency'`) được thiết kế với trọng số phạt khổng lồ ($C_{shed}$) để ép optimizer phải ưu tiên tận dụng mọi nguồn phát hoặc nhập điện từ MG khác thay vì cắt tải của khách hàng. Trọng số này (VOLL - Value of Lost Load) quy định ưu tiên cắt tải: $C_{shed}$ = 100,000 để bắt ép mô hình vét sạch công suất trước khi phải tự cắt điện.

### Ràng buộc Cứng (Hard Constraints) bảo vệ Critical Load
- Khai báo danh sách các nút phụ tải cực kỳ quan trọng (Critical Load Node) cho từng MG.
- Thiết lập ràng buộc cứng (Hard constraint): $P_{shed, critical} = 0$.
- **Cơ chế:** DSO hoặc thuật toán ATC không bao giờ ra lệnh trực tiếp cắt tải. Thay vào đó, ATC thay đổi giá bóng ($\lambda$) để tạo ra động lực kinh tế. Khi MG "khỏe" bị thu hút bởi giá cao, nó sẽ ép các tải không quan trọng nội bộ (Non-critical load) hy sinh một phần điện năng để lấy dư địa bơm công suất sang cứu MG "yếu" có các tải quan trọng bị đe dọa (để tránh vi phạm ràng buộc $P_{shed, critical} = 0$).

## 3. Thuật toán phân cấp ATC (Lớp 2)

Hệ thống đã thay thế hoàn toàn cấu trúc Flat P2P (ADMM) bằng kiến trúc Bi-level (ATC) giúp tốc độ hội tụ và độ tin cậy được đảm bảo hơn trong cứu nạn:
- **Biến Giao dịch $P_{trade}$:** Đại diện cho công suất chuyển giao giữa MG $i$ và MG $j$ trên đường dây liên kết (tie-line).
- **Virtual Target ($P_{target}$):** DSO dựa trên yêu cầu gửi lên từ các MG để tính toán mục tiêu chia sẻ $P_{target, ij} = \frac{P_{i \rightarrow j} - P_{j \rightarrow i}}{2}$.
- **Hệ số phạt (Augmented Lagrangian):** Hàm mục tiêu của từng MG được tích hợp thêm 2 thành phần phạt:
  - Phạt tuyến tính: $\lambda \times (P_{trade} - P_{target})$ (Đại diện cho tiền thanh toán thanh khoản - Shadow price).
  - Phạt bậc 2: $\frac{\rho}{2} \times (P_{trade} - P_{target})^2$ (Ép các MG phải tuân thủ nghiêm ngặt mục tiêu do DSO đề ra).

**Kỹ thuật Scaling (Chống lỗi Bang-Bang):** 
Bởi vì $\rho$ bị bình phương, nếu không chuẩn hóa, các biến số sẽ bị tràn hoặc quá nhỏ làm mất cân đối hàm mục tiêu. Mã nguồn hiện tại ép các giá trị $P_{trade}$, $\lambda$ trong hệ ATC sang **hệ per-unit (pu)**, và nhân với hệ số quy đổi biến khi đưa vào hàm mục tiêu ở Local MG (đang tính theo Cent/kW) để đảm bảo hội tụ vững chắc.

## 4. Kịch bản Mô phỏng Sự cố (Accident Scenario)
Trong mã nguồn, một cờ `stage='Emergency'` được cung cấp vào `build_microgrid_model`. Khi cờ này kích hoạt, hàm `apply_fault(time_fault=17)` sẽ can thiệp vào mô hình vật lý:
1. **Cô lập lưới (Islanded):** Chặn đứng khả năng lấy điện từ lưới chính (Main Grid) tại thời điểm $t=17$ (ví dụ: giới hạn luồng nhập về mức rất nhỏ hoặc bằng 0).
2. **Triệt tiêu nguồn phát (Loss of DG):** Đánh sập hoặc vô hiệu hóa các máy phát phân tán (DG) nội bộ bên trong MG yếu.
3. Sự kết hợp này vào thời điểm 5h chiều (mặt trời bắt đầu tắt, tải đạt đỉnh) tạo ra một kịch bản *Stress Test* cực đại. Nhờ vào thuật toán ATC, các MG lân cận sẽ nhận thấy sự chênh lệch $\lambda$ và phản ứng lại bằng cách dồn công suất qua đường dây Tie-line để cứu các nút tải quan trọng của MG bị lỗi.

---
*Tài liệu này phục vụ cho việc đối chiếu với các công bố khoa học (Literature Review) liên quan đến Resilience, ATC-SOCP, và Emergency Control System.*

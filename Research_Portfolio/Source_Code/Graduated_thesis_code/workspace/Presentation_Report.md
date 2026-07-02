# Báo Cáo Thuyết Trình: Hệ thống Chia sẻ Công suất Khẩn cấp (Emergency Power Sharing)
**Tiếp cận từ trên xuống (Top-Down Process)**

---

## 1. Sự tiến hóa của SOCP: Từ "Tối đa hóa Lợi nhuận" sang "Bảo vệ Phụ tải"
- **Phiên bản Cũ (Day-Ahead):** Ràng buộc luồng công suất SOCP (DistFlow) được chạy với mục tiêu tối ưu hóa kinh tế (Economic Dispatch). Hàm mục tiêu tập trung vào việc giảm thiểu chi phí phát điện và tối đa hóa lợi nhuận mua bán với lưới chính.
- **Phiên bản Mới (Emergency):** Khi sự cố xảy ra, Hàm mục tiêu được lột xác hoàn toàn. 
  - Hệ thống loại bỏ khái niệm "lợi nhuận" và chuyển sang **Tối thiểu hóa Cắt tải (Minimize Load Shedding)**.
  - Bằng cách gán một trọng số phạt khổng lồ $C_{shed}$ (Value of Lost Load), phương trình SOCP sử dụng đòn bẩy kinh tế để "bắt ép" mô hình vận hành: Nó sẵn sàng chạy các nguồn đắt tiền nhất (DG khởi động lạnh) hoặc mua điện giá cao qua P2P miễn là giữ được điện cho phụ tải.
  - **Bảo vệ Critical Load:** Thay vì dùng hard constraint (dễ gây lỗi Infeasible), hệ thống dùng Soft Penalty bằng cách đặt $C_{shed\_critical} = 100 \times C_{shed\_noncritical}$. Điều này ép các MG thà tự cắt điện tải thường của mình còn hơn để tải quan trọng ở MG khác bị sập.

---

## 2. Kiến trúc Điều phối: Tại sao ATC vượt trội so với ADMM trong Kịch bản Khẩn cấp?

So với thuật toán ADMM (Alternating Direction Method of Multipliers) vốn phổ biến trong giao dịch P2P thông thường, ATC (Analytical Target Cascading) thể hiện ưu thế vượt trội trong kịch bản mất lưới điện hoặc đứt đường dây liên kết (Contingencies) nhờ 3 yếu tố cốt lõi:

### A. Cấu trúc Liên kết & Độ bền Truyền thông (Communication Topology & Robustness)
- **ADMM (Cấu trúc Phẳng P2P - Peer-to-Peer Flat Topology):**
  - Đòi hỏi các Microgrid (MG) thương lượng trực tiếp với nhau, tạo ra số lượng liên kết truyền thông $O(N^2)$.
  - **Lỗ hổng:** Khi xảy ra sự cố vật lý (như đứt đường cáp kết nối P2P giữa MG1 và MG2), ma trận liên thông truyền thông bị phân tách. Sự gián đoạn này khiến quá trình đồng thuận (Consensus matrix) bị phá vỡ hoàn toàn, dẫn đến thuật toán ADMM không thể hội tụ (Divergence), làm sụp đổ toàn bộ việc chia sẻ công suất khẩn cấp.
- **ATC (Cấu trúc Ngôi sao Phân cấp - Hierarchical Star Topology):**
  - Thiết lập mô hình điều phối 2 cấp (Bi-level Optimization). Lưới chính (DSO) hoặc Virtual Market Hub đóng vai trò làm điều phối viên trung tâm (Upper-level Coordinator), các MG là cấp dưới (Lower-level).
  - Các MG hoàn toàn độc lập và chỉ giao tiếp $1:1$ với Coordinator trung tâm (Số lượng liên kết là $O(N)$). 
  - **Khả năng tự chữa lành (Self-healing):** Khi xảy ra sự cố đứt tieline vật lý, DSO nhận diện cấu trúc liên kết mới và ngay lập tức cập nhật ràng buộc kết nối, tự động tính toán lại các chỉ tiêu trao đổi công suất mục tiêu ($P_{target}$). Thuật toán ATC vẫn hội tụ bình thường do cấu trúc truyền thông trung tâm không bị ảnh hưởng bởi lỗi của các tuyến tieline nội bộ.

### B. Cơ chế Toán học và Lực ép Hội tụ Khẩn cấp (Mathematical Mechanism & Coercive Force)
Trong trường hợp khẩn cấp, mục tiêu tối thượng là **Tối thiểu hóa Cắt tải** chứ không còn là tối ưu hóa lợi nhuận. Sự khác biệt về mặt toán học giữa ADMM và ATC quyết định khả năng ứng cứu:
- **Hạn chế của ADMM:** ADMM cố gắng đưa các MG đến sự đồng thuận về lượng công suất giao dịch tại các điểm đấu nối thông qua cơ chế cập nhật biến kép (dual variable update). Khi xảy ra thảm họa, sự bất đối xứng nguồn - tải quá lớn (MG1, MG2 thiếu hụt nghiêm trọng, MG3, MG4 dư thừa công suất) khiến việc thương lượng phẳng không có "trọng tài" ép buộc. ADMM có thể bị kẹt trong quá trình lặp vô hạn hoặc dao động mạnh quanh biên giới hạn vật lý.
- **Sức mạnh cưỡng bức của ATC (Augmented Lagrangian Penalty):**
  - Hàm mục tiêu của MG $i$ trong ATC được bổ sung số hạng phạt bình phương khoảng cách đến mục tiêu điều phối:
    $$\min F_i(X_i) + \sum_{j \in \Omega_i} \left[ \lambda_{ij}^T (P_{ij} - P_{ij}^{target}) + \frac{\rho_{ij}}{2} \|P_{ij} - P_{ij}^{target}\|_2^2 \right]$$
  - Trong đó, $\lambda_{ij}$ đại diện cho **Giá bóng (Shadow Price)** và $\rho_{ij}$ là **Hệ số phạt (Penalty parameter)**.
  - Khi MG1 bị sự cố thiếu nguồn nặng, Coordinator trung tâm nhận thấy sự mất cân đối công suất. Nó sẽ tự động nâng cao $\lambda$ và $\rho$ tương ứng để áp đặt một "áp lực tài chính ảo" khổng lồ lên các MG còn lại. Lực phạt bậc hai $\frac{\rho}{2} \|P - P^{target}\|_2^2$ tăng cực nhanh khi dòng công suất lệch xa mục tiêu cứu hộ, ép buộc các MG khỏe mạnh (MG3, MG4) phải hy sinh lợi ích kinh tế tức thời để xả pin và khởi động máy phát diesel cứu trợ MG1, MG2.

### C. Bảo mật Thông tin và Khả năng Mở rộng (Information Privacy & Scalability)
- **ADMM:** Để giải quyết bài toán ràng buộc dòng công suất AC (SOCP DistFlow) trong mạng lưới P2P phẳng, các MG thường phải trao đổi các thông số nhạy cảm (như ma trận Jacobi, giá biên, hoặc cấu trúc tải nội bộ) với các lân cận để tính toán dòng công suất khả thi. Điều này vi phạm nghiêm trọng tính bảo mật thông tin.
- **ATC:** Đảm bảo **Bảo mật tuyệt đối (Maximum Privacy)**. Các MG chỉ gửi công suất trao đổi biên ($P_{ij}$) lên Coordinator. DSO giải bài toán tối ưu hóa lưới điện toàn cục và chỉ trả về $P_{target}$, $\lambda$, và $\rho$. Thông tin về cấu trúc phụ tải chi tiết, trạng thái pin (SOC), và chi phí phát điện DG của từng MG hoàn toàn được giữ kín trong nội bộ của MG đó. Đồng thời, cấu trúc phân cấp giúp giảm thời gian tính toán toàn cục, tăng khả năng mở rộng (Scalability) khi tích hợp thêm các MG mới.

---

## 3. MPC giải quyết bài toán Thời gian bằng 3 Pha (3-Phase Simulator) như thế nào?
Việc lập lịch tĩnh 24h (Static Day-ahead) hoàn toàn bất lực trước những sự kiện không lường trước. MPC (Rolling Horizon) xử lý triệt để lỗ hổng này qua 3 Pha vận hành:
- **Pha 1 (Pre-fault - Lập lịch tĩnh):** Hệ thống chạy một lần duy nhất trước ngày vận hành để chốt lịch chạy tối ưu kinh tế và tạo ra đường cong SOC kỳ vọng ($SOC_{DA}$).
- **Pha 2 (Emergency - MPC Cuộn thời gian thực):** Khi sự cố nổ ra tại $t_{fault}$, MPC lập tức nhảy vào can thiệp.
  - Nó không giải bài toán 24h nữa, mà chạy lùi từng bước một (Step-by-step). Tại mỗi giờ $t$, nó đo đạc trạng thái Pin thực tế $SOC_{actual}$ làm gốc.
  - **Tầm nhìn tương lai (Risk Awareness):** MPC dự báo $H$ bước tiếp theo, kết hợp **End-of-Horizon SOC Penalty** để phạt nặng nếu BESS bị xả kiệt. Nhờ vậy, pin không bị xả khô ngay trong giờ đầu tiên mà được "dè sẻn" để duy trì sinh tồn qua nhiều giờ mất điện.
- **Pha 3 (Post-fault - Khôi phục):** Ngay khi lưới điện kết nối lại, sự kiện kết thúc. Hệ thống ngay lập tức thoát khỏi vòng lặp MPC, lấy $SOC_{actual}$ hiện tại làm điểm neo mới, giải lại bài toán One-shot tĩnh để thiết lập một quỹ đạo Day-ahead mới, đưa toàn bộ 4 Microgrids về lại trạng thái tối ưu kinh tế.

---

## 4. Đề xuất Kịch bản Thử thách (Stress-Testing Scenarios)
Để chứng minh sự ưu việt của thuật toán ATC-MPC, mô hình cấu hình 4 kịch bản lỗi khốc liệt. **Mũi nhọn thảm họa sẽ đánh thẳng vào MG1 và MG2 (nhóm tải nặng)**, ép MG3 (nhiều Renewable) và MG4 (Máy phát Diesel) dốc toàn lực ứng cứu:
1. **Kịch bản 1 (Islanded):** Mất toàn bộ nguồn cấp từ Lưới chính. Đánh giá tính năng cắt ngàm PCC.
2. **Kịch bản 2 (Tie-line Fault):** Đứt đường dây liên kết P2P huyết mạch giữa MG1 và MG2. Đánh giá khả năng định tuyến lại dòng điện (Re-routing) của ATC.
3. **Kịch bản 3 (Loss of DER):** Mất toàn bộ năng lượng mặt trời (Solar) đột ngột.
4. **Kịch bản 4 (Thảm họa N-2):** Đứt lưới chính đồng thời chia cắt cụm. Đánh giá sinh tồn phân cụm độc lập (Clustering Survivability).

---

## 5. Danh mục các Biến & Tham số Mới trong Mô hình SOCP Nội bộ (Local SOCP Model)

Để hiện thực hóa các chiến lược chia sẻ công suất khẩn cấp, điều phối ATC và vận hành thời gian thực MPC có xét đến cân bằng công suất phản kháng (Q-Balance), mô hình SOCP cục bộ (`Function.py`) đã tích hợp thêm các biến và tham số chuyên dụng sau:

### A. Nhóm Biến Khẩn cấp & Cắt giảm Phụ tải (Load Shedding Optimization)
| Tên biến trong Code | Ký hiệu toán học | Kiểu dữ liệu (Pyomo) | Ý nghĩa vật lý & Hàm mục tiêu |
| :--- | :--- | :--- | :--- |
| **`P_shed[node, time]`** | $P^{shed}_{i, t}$ | `pe.Var` (NonNegativeReals) | Lượng công suất tác dụng sa thải tại nút $i$ thời điểm $t$. Được giải phóng ở chế độ khẩn cấp và bị phạt nặng bởi chi phí Value of Lost Load ($C_{shed}$). |
| **`q_shed_val`** *(Biểu thức)* | $Q^{shed}_{i, t}$ | `pe.Expression` | Lượng công suất phản kháng sa thải tự động tại nút $i$: $Q^{shed}_{i, t} = P^{shed}_{i, t} \times \left( \frac{Q^{load}_{i, t}}{P^{load}_{i, t}} \right)$ nhằm giữ nguyên hệ số công suất của tải. |

### B. Nhóm Biến bù bảo vệ BESS (BESS Risk Mitigation)
| Tên biến trong Code | Ký hiệu toán học | Kiểu dữ liệu (Pyomo) | Ý nghĩa vật lý & Hàm mục tiêu |
| :--- | :--- | :--- | :--- |
| **`SOC_slack[node]`** | $SOC^{slack}_{b}$ | `pe.Var` (NonNegativeReals) | Biến bù thể hiện độ lệch thiếu hụt của trạng thái sạc Pin thực tế ở cuối chu kỳ dự báo MPC ($SOC_{b, H-1}$) so với mốc tham chiếu Day-Ahead ($SOC^{DA}_{ref}$). Phạt bậc hai $\beta \times (SOC^{slack}_b)^2$ trong hàm mục tiêu để tránh pin bị xả cạn kiệt cận thị. |

### C. Nhóm Biến Phân rã Xuất khẩu Lưới (Grid Interface Splitting)
| Tên biến trong Code | Ký hiệu toán học | Kiểu dữ liệu (Pyomo) | Ý nghĩa vật lý & Giới hạn ràng buộc |
| :--- | :--- | :--- | :--- |
| **`P_neg_paid[time]`** | $P^{grid-}_{paid, t}$ | `pe.Var` (NonPositiveReals) | Lượng công suất xuất ngược lên lưới chính được thanh toán tiền điện theo biểu giá. Ràng buộc khống chế: $P^{grid-}_{paid, t} \ge -EXPORT\_LIMIT$. |
| **`P_neg_free[time]`** | $P^{grid-}_{free, t}$ | `pe.Var` (NonPositiveReals) | Lượng công suất xuất ngược vượt ngưỡng cho phép. Lượng điện này không được tính tiền (bán 0đ) để hạn chế các MG phát ồ ạt gây bất ổn lưới chính. |

### D. Nhóm Biến Công suất phản kháng của Máy phát (Reactive Power Support)
| Tên biến trong Code | Ký hiệu toán học | Kiểu dữ liệu (Pyomo) | Ý nghĩa vật lý & Giới hạn ràng buộc |
| :--- | :--- | :--- | :--- |
| **`Q_DG[node, time]`** | $Q^{DG}_{d, t}$ | `pe.Var` (NonNegativeReals) | Công suất phản kháng phát ra từ máy phát Diesel nhằm bù phản kháng nội bộ và giữ ổn định điện áp khi Microgrid bị tách đảo khẩn cấp. Khống chế bởi biểu đồ khả năng phát (Capability Curve) của DG. |

### E. Nhóm Tham số Điều phối ATC (ATC Parameters)
| Tên tham số trong Code | Ký hiệu toán học | Kiểu dữ liệu (Pyomo) | Ý nghĩa vật lý & Vai trò điều phối |
| :--- | :--- | :--- | :--- |
| **`P_target[node, time]`** | $P^{target}_{ij, t}$ | `pe.Param` (Mutable=True) | Công suất mục tiêu trao đổi qua tie-line $i-j$ do DSO (Coordinator cấp trên) tính toán và áp đặt xuống các MG cấp dưới. |
| **`lamda_ATC[node, time]`** | $\lambda_{ij, t}$ | `pe.Param` (Mutable=True) | Giá bóng (Shadow Price) thể hiện xu hướng cân bằng cung-cầu toàn hệ thống do DSO cập nhật. |
| **`rho_ATC[node, time]`** | $\rho_{ij, t}$ | `pe.Param` (Mutable=True) | Hệ số phạt bậc hai nhằm ép buộc các MG điều chỉnh công suất biên hội tụ nhanh chóng về mức $P_{target}$. |

---

*Tài liệu được trích xuất và tổng hợp tự động từ Base Code và Literature Summary (03/06/2026).*

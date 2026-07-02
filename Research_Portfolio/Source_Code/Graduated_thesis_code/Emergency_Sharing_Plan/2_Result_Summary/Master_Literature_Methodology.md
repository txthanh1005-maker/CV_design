# TỔNG HỢP TÀI LIỆU VÀ PHƯƠNG PHÁP LUẬN: CHIA SẺ CÔNG SUẤT KHẨN CẤP TRONG MULTI-MICROGRIDS 
*(Master Literature & Methodology)*

Tài liệu này tổng hợp cấu trúc phương pháp tiếp cận **Từ trên xuống (Top-Down)** cho việc chia sẻ công suất khẩn cấp, tích hợp các nghiên cứu tài liệu (Literature Review), kiến trúc điều khiển (System Architecture) và công thức toán học (Formulation).

## 1. TỔNG QUAN TÀI LIỆU VÀ KIẾN TRÚC HỆ THỐNG (SYSTEM ARCHITECTURE)

### 1.1. Khả năng phục hồi của Lưới điện & Multi-Microgrids (MMGs)
*   **Sự dịch chuyển Hệ chuẩn (Paradigm Shift):** Các nghiên cứu hiện đại nhấn mạnh sự chuyển dịch thiết yếu từ "Độ tin cậy" (Reliability - giảm thiểu tần suất mất điện) sang **Khả năng phục hồi (Resilience)** nhằm sinh tồn và khôi phục từ các sự kiện cực đoan có xác suất thấp nhưng hậu quả cao.
*   **Vai trò của MMGs & Chế độ cô lập:** Khi lưới truyền tải chính bị sập, các lưới phân phối phải chuyển đổi liền mạch sang **Chế độ cô lập (Islanded Mode)**. Vì một microgrid đơn lẻ thường thiếu hụt tài nguyên để tự sinh tồn, **Chia sẻ Công suất Khẩn cấp (Emergency Power Sharing)** giữa các MMGs nối mạng là giải pháp cốt lõi. Các MG khỏe mạnh xuất năng lượng dư thừa cho MG bị lỗi, ngăn ngừa mất điện dây chuyền.
*   **Bảo vệ Phụ tải Quan trọng:** Trái với mô hình cũ, hệ thống hiện tại phân biệt rất nghiêm ngặt giữa phụ tải thường và phụ tải quan trọng (Critical loads - ví dụ: Bệnh viện, trạm liên lạc), buộc phải được bảo vệ bằng mọi giá.

### 1.2. Kiến trúc Hệ thống: Vận hành Hai Lớp (Dual-Layer Operation) & Phân loại Microgrid
Dựa trên bài báo *"Two-stage distributed fault recovery for multi-microgrid distribution networks"*, hệ thống chia lưới điện thành 2 giai đoạn (Giai đoạn cảnh báo và Phân chia đảo) và phân loại MG thành 3 loại (Load-type, Resource-type, ES-type) để ưu tiên ghép cặp (Pre-pairing), hỗ trợ thuật toán chia sẻ khẩn cấp hội tụ nhanh hơn.
Kiến trúc tổng thể được chia làm 2 vòng đời vận hành rõ rệt:
*   **Chế độ Bình thường (Day-ahead Scheduling):** Chạy một vòng duy nhất trước ngày vận hành cho khung thời gian 24h. Tối đa hóa lợi nhuận kinh tế (Economic Dispatch). Đầu ra cốt lõi là Lịch bật/tắt (Unit Commitment) và **Đường cong kỳ vọng SOC của BESS ($SOC_{DA}$)**. Lớp này độc lập và được bảo tồn hoàn toàn.
*   **Chế độ Khẩn cấp (Emergency MPC Mode):** Kích hoạt khi có sự cố tại $t_{fault}$. Xây dựng một Coordinator (`ATC_Global_model_mpc`) và hệ thống Local hoàn toàn mới. Hàm mục tiêu chuyển sang **Tối thiểu hóa Cắt tải** và duy trì **Hàm phạt SOC**.
*   **Cơ chế Thoát khỏi Khẩn cấp (Restoration / Exit Strategy):** Khi lưới chính kết nối lại, hệ thống ngay lập tức ngắt vòng lặp MPC, chuyển hàm mục tiêu về lại Max Profit. Nó lấy $SOC_{actual}$ thực tế hiện tại làm điểm neo, chạy vòng tính toán One-shot cho các giờ còn lại để bù lại lượng pin hao hụt một cách tối ưu kinh tế.

### 1.3. Điều khiển Động qua MPC và Sự linh hoạt không gian
*   **Vượt qua Lập lịch Tĩnh bằng MPC:** Lập lịch Day-Ahead tĩnh không thể thích ứng với đứt dây hay mất nguồn đột ngột. Kế thừa từ bài báo *"Optimal scheduling of virtual power plant with mobile energy storage for power grid resilience improvement"*, hệ thống áp dụng cơ chế **Điều khiển Dự báo Mô hình (MPC)** hoặc Tối ưu hóa Chân trời Cuộn (Rolling Horizon).
*   **Ý thức Rủi ro (Risk Awareness) & Dè sẻn năng lượng:** MPC liên tục cập nhật sai số và "đóng băng" trạng thái thực tế (nhất là $SOC_{actual}$). Dựa trên "Endowment effect", hệ thống ngăn chặn xả cạn kiệt pin bằng cách đặt các ngưỡng penalty cứng/mềm nhằm bảo vệ sinh tồn dài hạn.
*   **Lưu trữ Di động (MES):** Một đóng góp mở rộng về yếu tố Không gian - Thời gian là sử dụng xe năng lượng (Mobile Energy Storage) có khả năng di chuyển vật lý giữa các MG trong mạng, gia tăng tính linh hoạt.

### 1.4. Điều phối Phân cấp qua Analytical Target Cascading (ATC)
*   **Sự vượt trội của ATC so với ADMM:** Một bộ điều khiển trung tâm duy nhất dễ bị tổn thương. ADMM giao tiếp "phẳng" đòi hỏi chéo $O(N^2)$ links, gây chậm trễ và dễ vỡ mạng khi cáp đứt. ATC cung cấp cấu trúc hình sao (Hierarchical / Star Topology) tạo thành Virtual P2P Market Hub.
*   **Cấu trúc Lớp trên (DSO) - Lớp dưới (MGs):** Bài báo *"Hierarchical Optimization Scheduling Model of Multi-Microgrids Based on Analytical Target Cascading"* khẳng định hiệu quả của ATC trong tách biệt xung đột lợi ích (Conflict of interest). MG chỉ gửi $P_{trade}$ lên Hub (bảo mật riêng tư). Coordinator dùng Giá bóng (Shadow Prices $\lambda$) để ép chia sẻ điện, hội tụ siêu tốc qua tính toán song song (Iterative Parallelism).
*   **ATC Vật lý và Thuật toán:** Trong lưới truyền tải, ATC (Available Transfer Capability) đo lường giới hạn vật lý để định tuyến công suất an toàn. Trong khi thuật toán ATC (Analytical Target Cascading) giúp cách ly sự cố (Fault Isolation), ngăn truyền tải sai lệch (FDI attacks) lây lan ra toàn hệ thống. Cả hai tạo nên khả năng phục hồi toàn diện.

---

## 2. CÔNG THỨC TOÁN HỌC (FORMULATION)

### 2.1. Đảm bảo Tính Khả thi bằng Nới lỏng SOCP (Second-Order Cone Programming)
Phương trình AC (DistFlow) phi tuyến, không lồi được nới lỏng bằng SOCP để đảm bảo lệnh chia sẻ của ATC tuân thủ định luật Kirchhoff, tránh sụt áp hoặc quá tải nhiệt, và tìm được điểm tối ưu toàn cục.
*   **Cân bằng Năng lượng (Nodal Power Balance):**
    $$ P_{n,t} - r_n \ell_{n,t} + I_{n}^{DG} P_{n,t}^{DG} + P_{n,t}^{RE} + P_{n,t}^{dis} - P_{n,t}^{chg} + P_{n,t}^{trade} = P_{n,t}^{Load} + \sum_{j \in \Lambda_n} P_{j,t} $$
    $$ Q_{n,t} - x_n \ell_{n,t} + I_{n}^{DG} Q_{n,t}^{DG} + Q_{n,t}^{BESS} = Q_{n,t}^{Load} + \sum_{j \in \Lambda_n} Q_{j,t} $$
*   **Vật lý Mạng và Nới lỏng SOCP (Network Physics & SOCP Relaxation):**
    $$ U_{m,t} - U_{n,t} = 2(r_n P_{n,t} + x_n Q_{n,t}) - (r_n^2 + x_n^2)\ell_{n,t} $$
    $$ \left\| \begin{matrix} 2P_{n,t} \\ 2Q_{n,t} \\ U_{m,t} - \ell_{n,t} \end{matrix} \right\|_2 \le U_{m,t} + \ell_{n,t} $$
*   **Giới hạn Vận hành (Operational Constraints):**
    $$ (V_{min})^2 \le U_{n,t} \le (V_{max})^2 $$
    $$ 0 \le \ell_{n,t} \le (I_{max,n})^2 $$
    $$ SOC_{n,t} = SOC_{n,t-1} + (\eta_{chg} P_{n,t}^{chg} - P_{n,t}^{dis}/\eta_{dis}) / E_{cap} $$

### 2.2. Mô phỏng Toán học Sự cố Lưới điện (Mathematical Simulation of Grid Errors)
*   **Mất Nguồn (Loss of Generation Source):** Sự cố tại thời điểm $t_{fault}$ tại node $n$:
    $$ I_{n,t}^{DG} = 0, \quad \bar{P}_{n}^{DG} = 0 \quad \forall t \ge t_{fault} $$
*   **Đứt Đường dây (Loss of Transmission Line):** 
    $$ P_{n,t} = 0, \quad Q_{n,t} = 0, \quad \ell_{n,t} = 0 \quad \forall t \ge t_{fault} $$
*   **Tấn công Mạng (Cyber Attacks):**
    *   **False Data Injection (FDI):** $$ \tilde{P}_{n,t}^{Load} = P_{n,t}^{Load} + \Delta P_{attack} $$
    *   **Mất kết nối:** Gián đoạn thông tin khiến điều kiện biên $P_{i,j,t} + P_{j,i,t} = 0$ thất bại.

### 2.3. Cấu trúc ATC Hai lớp & Hàm Phạt (Bi-level ATC Structure & Penalty)
*   **Hàm Phạt Augmented Lagrangian:** Tối thiểu hóa sai lệch giữa công suất DSO yêu cầu và MG đáp ứng.
    $$ \pi = \lambda (P_{tie}^{DSO} - P_{tie}^{MG}) + \| \rho \circ (P_{tie}^{DSO} - P_{tie}^{MG}) \|_2^2 $$
    Cập nhật qua mỗi vòng lặp $k$:
    $$ \lambda^{(k+1)} = \lambda^{(k)} + 2 \rho^{(k)} \circ \rho^{(k)} \circ (P_{tie}^{DSO,(k)} - P_{tie}^{MG,(k)}) $$
    $$ \rho^{(k+1)} = \beta \rho^{(k)} $$
*   **Hàm Phạt SOC ở cuối cửa sổ H (End-of-Horizon SOC Penalty):** Triệt tiêu hiện tượng thiển cận (myopic) của MPC ở cuối cửa sổ $H$:
    $$ Penalty_{SOC} = \beta \cdot \max(0, SOC_{DA}(t+H) - SOC_{MPC}(t+H))^2 $$
*   **Hệ thống Trọng số Ưu tiên (Weight Hierarchy):**
    $$ C_{PV/Wind} < SOC\_Penalty < C_{tie\_line} < C_{shed\_non\_critical} \ll C_{critical\_shed} $$

### 2.4. Công thức Cắt Tải Khẩn Cấp (Load Shedding Formulation)
Đảm bảo 100% phụ tải quan trọng (Critical Loads) sống sót bằng các ràng buộc cứng:
*   **Cân bằng Công suất khi Cắt Tải:**
    $$ P_{n,t}^{in} + P_{n,t}^{DG} + P_{n,t}^{dis} = P_{n,t}^{out} + P_{n,t}^{chg} + (P_{n,t}^{Load,critical} - P_{shed,n,t}^{critical}) + (P_{n,t}^{Load,non\_critical} - P_{shed,n,t}^{non\_critical}) $$
*   **Ràng buộc Phân loại Cắt tải:**
    $$ P_{shed,n,t}^{critical} = 0 \quad \forall n, t $$
    $$ 0 \le P_{shed,n,t}^{non\_critical} \le P_{n,t}^{Load,non\_critical} $$

### 2.5. Chỉ số Khả năng Phục hồi (Resilience Metrics)
*   **Khả năng sinh tồn (Survivability):** Phần trăm phụ tải được phục vụ trong thời gian sự cố.
    $$ \text{Resilience}_{load} = 1 - \frac{\sum_{t=t_e}^{t_r} \sum_{n} P_{shed,n,t}}{\sum_{t=t_e}^{t_r} \sum_{n} P_{n,t}^{Load}} $$
*   **Tốc độ phục hồi (Rapidity):**
    $$ T_{recovery} = t_{restored} - t_{event} $$
*   **Hình thang Phục hồi (Resilience Trapezoid):** Diện tích dưới đường cong hiệu suất.
    $$ R = \int_{t_{event}}^{t_{restored}} \Phi(t) dt $$

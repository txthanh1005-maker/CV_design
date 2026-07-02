# Báo cáo Khảo sát: Phương pháp Phân bổ Tải Quan trọng (Critical Load) trong Microgrid

## 1. Đặt vấn đề
Trong mô hình tối ưu hóa vận hành Microgrid sử dụng Model Predictive Control (MPC) và Second-Order Cone Programming (SOCP), việc cắt tải (load shedding) trong các kịch bản sự cố là một chiến lược quan trọng để giữ vững ổn định hệ thống. Bài toán đặt ra là cấu hình tải quan trọng theo 2 phương án:
- **Phương án 1:** 20% số lượng nodes trong hệ thống là tải quan trọng (không được cắt), 80% nodes còn lại có thể cắt hoàn toàn.
- **Phương án 2:** 20% công suất tại *mỗi* node là tải quan trọng, 80% công suất còn lại ở node đó có thể bị cắt (Demand Response).

Dựa trên việc đối chiếu với các nghiên cứu và mô hình SOCP chuẩn (IEEE/OpenAlex), dưới đây là phân tích ưu/nhược điểm của 2 phương án.

## 2. Phân tích Ưu/Nhược điểm

### 2.1 Phương án 1: 20% số lượng nodes là tải quan trọng
Về mặt mô hình toán học (SOCP/MPC):
- Biến cắt tải $P_{shed, i}$: Với các node quan trọng (20%), $P_{shed, i} = 0$. Với các node thường (80%), $0 \le P_{shed, i} \le P_{load, i}$.
- **Ưu điểm thực tế:** Phản ánh đúng hạ tầng lưới điện phân phối truyền thống. Các tải quan trọng (bệnh viện, trung tâm dữ liệu, trạm cứu hỏa) thường tập trung tại một số node cụ thể và được bảo vệ ở mức nhánh (feeder level). Việc cắt tải chỉ yêu cầu đóng/cắt CB (Circuit Breaker) tại đầu node.
- **Nhược điểm toán học & vận hành:** Cắt 100% tải ở 80% số node sẽ làm thay đổi đột ngột dòng công suất (power flow), tạo ra sự chênh lệch áp lớn giữa các vùng trong lưới. Sự phân bố tải không đồng đều có thể làm giảm độ chặt (tightness) của lưới SOCP relaxation (DistFlow) do dòng điện trên một số nhánh có thể thay đổi cực đoan.

### 2.2 Phương án 2: 20% công suất tại *mỗi* node là tải quan trọng
Về mặt mô hình toán học (SOCP/MPC):
- Biến cắt tải $P_{shed, i}$: Tại tất cả các node, $0 \le P_{shed, i} \le 0.8 P_{load, i}$.
- **Ưu điểm toán học & vận hành:** Đảm bảo tất cả các node đều duy trì một lượng tải tối thiểu. Dòng công suất phân bố đồng đều hơn, giúp biên độ điện áp (voltage profile) trơn tru và ổn định. Sự đồng đều này giúp bộ giải (solver) như Gurobi/IPOPT hội tụ nhanh hơn trong thuật toán MPC và duy trì SOCP relaxation ở trạng thái chính xác cao nhất (exactness).
- **Nhược điểm thực tế:** Đòi hỏi hạ tầng lưới điện thông minh (Smart Grid) với cơ sở hạ tầng đo lường tiên tiến (AMI) và công nghệ Đáp ứng nhu cầu (Demand Response) tới từng hộ gia đình. Hệ thống phải có khả năng bóc tách để ngắt thiết bị tiêu thụ điện năng lớn (điều hòa, sạc EV) trong khi vẫn duy trì các thiết bị thiết yếu (đèn, tủ lạnh) ở mọi điểm nút.

## 3. Độ Phức Tạp Toán Học (Mathematical Complexity)
Cả hai phương án đều **không làm tăng độ phức tạp thuật toán** vì chúng chỉ thay đổi giá trị biên (upper bounds) của các biến liên tục (continuous variables). Cụ thể:
- Không sinh ra biến nguyên (integer variables) nếu giả định việc cắt tải là liên tục, từ đó tránh được sự gia tăng phức tạp tính toán của MISOCP.
- Hoàn toàn giữ được tính lồi (convexity) của bài toán SOCP.
Tuy nhiên, Phương án 2 giúp lưới điện cân bằng hơn, giảm rủi ro ma trận Jacobian bị "ill-conditioned" trong các bước giải nội dòng của bộ giải.

## 4. Kết luận & Đề xuất Áp dụng
**Đề xuất tối ưu:** Chọn **Phương án 2 (20% công suất tại mỗi node là tải quan trọng)** cho dự án sử dụng mô hình MPC & SOCP.

**Lý do:** 
1. Microgrid là hệ thống đại diện cho mô hình lưới điện hiện đại (Smart Grid). Việc áp dụng mô hình phân bổ tải cục bộ tại từng node (Demand Response / Smart Load Shedding) là xu hướng nghiên cứu đang được chú trọng trên IEEE.
2. Từ góc nhìn tối ưu toán học SOCP, việc duy trì một tỷ lệ phân bổ tải đồng đều trên tất cả các node giúp giảm hiện tượng sụt áp cục bộ và đảm bảo sự hội tụ mượt mà (smooth convergence) qua các khung thời gian (rolling horizon) của thuật toán MPC.

## 5. Tài liệu tham khảo
- J. Taylor, "Convex Optimization of Power Systems", Cambridge University Press, 2015. (Cơ sở lý thuyết cho DistFlow SOCP relaxation)
- "A Risk-Averse Conic Model for Networked Microgrids Planning With Reconfiguration and Reorganizations," IEEE, 2019 (Phân tích sự ảnh hưởng của thay đổi topo mạng lưới lên hệ SOCP).
- "Energy Management System for an Islanded Microgrid With Convex Relaxation," 2019 (Khẳng định độ ưu việt và độ chặt của SOCP trong môi trường Microgrid khi có load shedding liên tục).
- Các dữ liệu siêu dữ liệu từ OpenAlex API về xu hướng "load shedding microgrid SOCP".

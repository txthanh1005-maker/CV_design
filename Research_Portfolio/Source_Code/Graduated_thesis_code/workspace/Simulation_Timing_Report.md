# Báo cáo Thời gian Thực thi Mô phỏng (Simulation Timing Report)

Tài liệu này ghi nhận thời gian tính toán thực tế (Wall-clock time) của thuật toán Distributed Model Predictive Control (MPC) sử dụng bộ giải Gurobi/IPOPT thông qua cấu trúc Analytical Target Cascading (ATC). Dữ liệu này dùng để đánh giá hiệu năng thuật toán và làm minh chứng cho sự cần thiết của các kỹ thuật tối ưu hóa nâng cao.

## 1. Kịch bản 1: Mất Nguồn Năng lượng Tái tạo (PV Loss)
- **Cấu hình Sự cố:** Mất 100% công suất PV tại MG1 trong giờ cao điểm bức xạ Mặt trời ($t=10$ đến $t=14$). Các lưới Microgrid vẫn giữ kết nối với Lưới điện chính (Main Grid).
- **Thời điểm Bắt đầu:** `15:39:31`
- **Thời điểm Kết thúc:** `15:49:58`
- **Tổng thời gian chạy:** **~10 phút 27 giây**
- **Đánh giá:** 
  - Hệ thống duy trì sự ổn định tuyệt đối.
  - Số bước lặp (ATC Iterations) trung bình để đạt trạng thái hội tụ (Converged) ở mỗi khung giờ là từ **21 đến 25 bước**.
  - Nhờ có Lưới chính làm điểm neo (slack bus) điều tần và cấp bù công suất, sự bù đắp qua giao dịch P2P diễn ra mượt mà và tiêu tốn ít thời gian tính toán.

## 2. Kịch bản 2: Thảm họa kép N-2 (Cascading Grid Loss + PV Loss)
- **Cấu hình Sự cố:** 
  - N-1: MG1 và MG2 bị đứt kết nối Lưới chính (Islanded mode) từ $t=8$ đến $t=14$.
  - N-2: Mất 100% PV tại MG1 và MG2 vào giờ cao điểm ($t=10$ đến $t=14$).
- **Thời điểm Bắt đầu:** `16:00:51`
- **Thời điểm Kết thúc:** `16:44:10`
- **Tổng thời gian chạy:** **~43 phút 19 giây**
- **Đánh giá:**
  - Thời gian tính toán **tăng đột biến gấp 4 lần**.
  - Sự cô lập hoàn toàn khỏi lưới điện chính buộc hệ thống phải tự thân cân bằng cung cầu nội bộ (chỉ dựa vào BESS, Wind, DG và nguồn dự trữ của MG3, MG4).
  - Tại đỉnh điểm của cú sốc ($t=10$), thuật toán MPC đã phải thực hiện tới **76 bước lặp ATC** mới có thể tìm ra được điểm cân bằng giá (Lambda) và chốt thỏa thuận giao dịch năng lượng giữa các MG.

## 3. Kết luận & Đề xuất Hướng tối ưu (Future Work)
Sự chênh lệch từ 10 phút lên 43 phút làm nổi bật một nhược điểm cố hữu của thuật toán phân tán (Decentralized/Distributed) khi đối mặt với điều kiện khắc nghiệt (Islanded + N-2). Ở các điều kiện này, điểm xuất phát của các biến đối ngẫu (Lagrangian multipliers) bị sai lệch quá lớn so với điểm tối ưu mới.

**Đề xuất:** Đây là cơ sở khoa học vững chắc để triển khai **Kỹ thuật Warm-Start** trong thuật toán Rolling Horizon MPC. Bằng cách kế thừa (inherit) các giá trị định giá `lamda`, lượng giao dịch `P_target` và hệ số phạt `rho_ATC` từ cửa sổ dự báo của giờ trước ($t-1$) làm điểm neo khởi tạo cho giờ hiện tại ($t$), chúng ta có thể loại bỏ thời gian leo dốc của thuật toán, kỳ vọng kéo giảm số bước lặp từ 76 xuống dưới 20 bước, qua đó đưa thời gian mô phỏng tổng thể quay về mức ~10 phút.

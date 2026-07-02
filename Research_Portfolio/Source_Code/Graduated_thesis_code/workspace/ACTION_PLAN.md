# ACTION PLAN - XỬ LÝ CÁC TÁC VỤ TỒN ĐỌNG (BACKLOG TỪ 02/06 - 08/06)

*Do các hạng mục từ ngày 02/06 đến 08/06 vẫn chưa hoàn thành, chúng ta cần tập trung toàn lực (Sprint 3 & 4) để chốt sổ toàn bộ Code và Số liệu, đồng thời tăng tốc viết Báo cáo để kịp nộp Draft 1 (09/06). Dưới đây là kế hoạch chi tiết để hoàn tất chúng.*

## Task 0.1: Khảo sát tài liệu (Literature Review) về Phân bổ Tải quan trọng (Critical Load)
- **Tình trạng:** `[x] DONE`
- **Agent phụ trách:** `agents/researcher.md`
- **Chi tiết thực thi:**
  - Tìm kiếm bài báo chuẩn IEEE/Science Direct (qua OpenAlex/ArXiv API) để so sánh và đánh giá 2 phương án của GVHD về tải quan trọng:
    1. Chọn 20% số lượng nodes trong hệ thống.
    2. Đặt 20% công suất tại *mỗi* node.
  - Phân tích ưu/nhược điểm (tính thực tế, độ phức tạp toán học) và đưa ra kết luận phương pháp áp dụng tối ưu nhất.
- **Tiêu chí nghiệm thu:** File báo cáo `workspace/Critical_Load_Research.md` kết luận phương án cấu hình tải quan trọng, kèm trích dẫn tài liệu tham khảo.

## Task 0.2: Khảo sát tài liệu (Literature Review) về Kịch bản Sự cố (Fault Scenarios)
- **Tình trạng:** `[x] DONE`
- **Agent phụ trách:** `agents/researcher.md`
- **Chi tiết thực thi:**
  - Nghiên cứu chi tiết các loại sự cố (ví dụ: đứt liên kết lưới chính, hỏng nguồn phát DG, đứt đường dây P2P, k-1/k-2 contingencies) thường được dùng để Stress-Test lưới điện Microgrid theo các nghiên cứu trên IEEE/Science Direct.
  - Rút ra kết luận xem nên áp dụng các loại lỗi nào vào dự án hiện tại để chứng minh độ bền bỉ (resilience) của mô hình MPC.
- **Tiêu chí nghiệm thu:** File báo cáo `workspace/Fault_Scenarios_Research.md` liệt kê các kịch bản sự cố tiêu chuẩn và đề xuất áp dụng, kèm trích dẫn tài liệu tham khảo.

## Task 0.3: Khảo sát bổ sung về Động lực học Sự cố trong hệ thống 4 Microgrid
- **Tình trạng:** `[x] DONE`
- **Agent phụ trách:** `agents/researcher.md`
- **Chi tiết thực thi:**
  - Tìm kiếm tài liệu IEEE/ScienceDirect để xác định trong hệ thống nhiều Microgrid (cụ thể là 4 MG), sự cố sụt giảm Năng lượng tái tạo (RE drop) hoặc đứt liên kết nên xảy ra ở bao nhiêu MG (1, 2, hay toàn bộ 4 MG)?
  - Phân tích xem sự cố nên diễn ra đồng thời (immediately/simultaneously) hay lan truyền từ từ (continuously/cascading).
  - Đánh giá cách tiếp cận nào phù hợp nhất để thể hiện năng lực của thuật toán MPC phân tán.
- **Tiêu chí nghiệm thu:** Báo cáo bổ sung vào `workspace/Fault_Scenarios_Research.md` (Phần 3.1) về động lực học sự cố.

## Task 1: Chốt Kịch bản Sự cố (Fault Scenarios) & Stress-Test MPC
- **Tình trạng:** `[x] DONE`
- **Agent phụ trách:** `agents/code_generator.md`
- **Chi tiết thực thi:**
  - Cập nhật Kịch bản C (Cascading RE Drop trên MG1, MG2) vào biến `fault_configs` trong file `main.py`.
  - Cập nhật và fix lỗi nhận diện biến `P_WT` sang `P_Wind` trong hàm `apply_custom_fault` tại file `Function.py`.
  - Chạy toàn bộ tiến trình mô phỏng MPC. Thuật toán đã chạy thành công, tìm được nghiệm tối ưu và hội tụ ở tất cả các khung giờ từ $t=12$ đến $t=23$.
- **Tiêu chí nghiệm thu:** Code chạy mượt mà không văng lỗi Infeasible. Các log xuất ra chứng minh lưới giữ được ổn định trong pha khẩn cấp và phục hồi.

## Task 2: Tối ưu Tốc độ Hội tụ (Warm-Start Algorithmic Optimization)
- **Tình trạng:** `[x] DONE`
- **Người phụ trách:** `agents/code_generator.md`
- **Chi tiết thực thi:**
  - Áp dụng kỹ thuật Hybrid Warm-Start cho thuật toán ATC trong quá trình Rolling Horizon.
  - Sửa `run_MPC_simulation` trong `main.py` để lưu trữ `warm_start_data` (từ Day-Ahead cho giờ đầu tiên, từ t-1 cho các giờ tiếp theo).
  - Áp dụng Adaptive Initial Rho (tăng rho khởi tạo trong pha khẩn cấp khi có thiếu hụt để bù đắp C_shed = 500,000).
  - Truyền `warm_start_data` vào `ATC_Global_model_mpc` ở `build_model.py` để làm Initial Guess cho vòng lặp tiếp theo, giúp giảm số bước hội tụ từ 70+ xuống còn 10-20 vòng trong những giờ khẩn cấp.
- **Tiêu chí nghiệm thu:** Thuật toán chạy nhanh hơn rõ rệt (giảm tổng số Iterations) mà nghiệm vẫn chính xác.

## Task 3: Xuất Đồ thị và Phân tích Dữ liệu (Result Visualization)
### Task 3.1: Khảo sát IEEE về Base Case & Các loại Đồ thị chuẩn
- **Tình trạng:** `[x] DONE`
- **Agent phụ trách:** `agents/researcher.md`
- **Chi tiết thực thi:**
  - Nghiên cứu các bài báo trên IEEE / ScienceDirect về "Networked Microgrids P2P trading MPC".
  - Xác định các loại biểu đồ (results) tiêu chuẩn cần phải có để chứng minh hiệu quả.
  - Đề xuất Base Case (ví dụ: Isolated mode, hoặc không có MPC) để so sánh và làm nổi bật sự cải thiện của thuật toán (Improvement).
- **Tiêu chí nghiệm thu:** Trình bày tóm tắt (Top-down approach) vào file `workspace/Result_Visualization_Research.md`.

### Task 3.2: Lập trình Xuất dữ liệu & Vẽ Đồ thị
- **Tình trạng:** `[x] DONE`
- **Agent phụ trách:** `agents/code_generator.md`
- **Chi tiết thực thi:**
  - Dựa trên kết quả Task 3.1, viết script trích xuất dữ liệu Gurobi/IPOPT ra file CSV.
  - Vẽ đồ thị Power Flow (P2P), BESS SOC, và Load Shedding (Critical vs Normal).
- **Tiêu chí nghiệm thu:** Bộ đồ thị hoàn chỉnh cho pha Khẩn cấp và Phục hồi. Các file ảnh `.png` đồ thị sắc nét mô tả hành vi của hệ thống trong 24h xuất hiện trong `Result_data/`.

## Task 4: Chạy Benchmark - So sánh với Tầm nhìn hoàn hảo (Perfect Foresight)
- **Tình trạng:** `[ ] TODO`
- **Agent phụ trách:** `agents/code_generator.md`
- **Chi tiết thực thi:**
  - Chạy mô phỏng Perfect Foresight (giả định Day-ahead biết trước sự cố) để lấy kết quả chuẩn.
  - So sánh kết quả của thuật toán MPC hiện tại so với Perfect Foresight để tính Optimality Gap.
- **Tiêu chí nghiệm thu:** Có số liệu so sánh chi phí vận hành & lượng tải bị cắt giữa 2 mô hình.

## Task 5: Đóng băng Code & Chốt Số liệu (DEADLINE 1)
- **Tình trạng:** `[ ] TODO`
- **Agent phụ trách:** `Meta-Agent (CEO)`
- **Chi tiết thực thi:**
  - Gom toàn bộ dữ liệu Output vào thư mục `Result_data/`.
  - Không sửa thêm logic cốt lõi. Sẵn sàng số liệu để viết báo cáo.
- **Tiêu chí nghiệm thu:** Dự án chuyển trạng thái sang Viết Báo Cáo.

## Task 5: Viết Intro, Literature Review, Math Formulation (Sprint 4)
- **Tình trạng:** `[ ] TODO`
- **Agent phụ trách:** `agents/latex_writer.md`
- **Chi tiết thực thi:**
  - Soạn thảo nội dung các phần: Introduction, Literature Review, và Mathematical Formulation.
  - Trích xuất thông số toán học từ `Function.py` để trình bày rõ quá trình SOCP Relaxation và MPC.
- **Tiêu chí nghiệm thu:** Các phần nội dung được hoàn thành thành các file nháp lưu trong `workspace/`.

## Task 6: Viết Case Study & Analysis dựa trên Stress-Test (Sprint 4)
- **Tình trạng:** `[ ] TODO`
- **Agent phụ trách:** `agents/latex_writer.md`
- **Chi tiết thực thi:**
  - Phân tích chi tiết kết quả mô phỏng (Task 1 & Task 2) để viết báo cáo.
  - Nhấn mạnh vào Benchmark Performance (Task 3).
- **Tiêu chí nghiệm thu:** Nội dung phân tích số liệu hoàn chỉnh, chuẩn bị sẵn sàng nộp Draft 1 cho GVHD (09/06).

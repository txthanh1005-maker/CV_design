# Cấu trúc Bố cục PowerPoint (Top-Down Approach)
**Dành cho buổi họp với GVHD (Ngày 03/06/2026)**
*Bố cục này phản chiếu chính xác cấu trúc Top-Down từ báo cáo `Presentation_Report.md`, kết hợp trình bày song song Mã nguồn (Code Implementation).*

---

## Slide 1: Tiêu đề (Title Slide)
- **Tiêu đề:** Chia sẻ công suất khẩn cấp cho hệ thống đa lưới điện siêu nhỏ (Multi-Microgrids) dựa trên ATC-SOCP và MPC.
- **Trình bày:** Trịnh Xuân Thành.
- **Mục tiêu buổi họp:** Trình bày lý thuyết cốt lõi, chạy Demo Code và chốt kịch bản thử nghiệm (Stress-Testing).

## Slide 2: Phương pháp Tiếp cận Top-Down (Overview)
*Giải thích với GVHD cách hệ thống giải quyết vấn đề từ vĩ mô xuống vi mô.*
- **Lớp Mạng lưới (Top Level - Không gian):** Điều phối toàn hệ thống bằng **ATC** (Thay thế ADMM).
- **Lớp Tối ưu Nội bộ (Bottom Level - Vật lý):** Chuyển dịch mục tiêu **SOCP** từ Tối ưu Kinh tế sang Bảo vệ Phụ tải.
- **Lớp Vận hành (Temporal Level - Thời gian):** Quản trị rủi ro bằng **MPC 3 Pha**.

## Slide 3: [Top Level] Kiến trúc Điều phối ATC vs Sự bế tắc của ADMM
- **Lý thuyết:** Khi có đứt cáp, mạng lưới P2P phẳng của ADMM ($O(N^2)$) sẽ mất kết nối và không thể hội tụ. ATC giải quyết bằng cấu trúc hình sao (DSO làm trung tâm). DSO áp **Giá bóng ($\lambda$)** xuống để điều hướng (re-route) điện năng cứu trợ.
- **💻 Triển khai Mã nguồn:**
  - Xóa bỏ hoàn toàn hàm mục tiêu cũ của ADMM. 
  - Khai báo biến `lamda_ATC`, `rho` và tạo phương trình phạt động `model.OBJ_ATC` ép trực tiếp vào vòng lặp điều phối của Lớp 1 (`build_model.py`).

## Slide 4: [Bottom Level] SOCP & Đòn bẩy Kinh tế Bảo vệ Tải
- **Lý thuyết:** Lột xác hoàn toàn mục tiêu của SOCP. Thay vì dùng ràng buộc cứng ($P_{shed\_critical} = 0$) làm solver bị lỗi Infeasible, ta dùng **Đòn bẩy Kinh tế (Soft Penalty)**. Áp đặt $C_{shed\_critical} = 100 \times C_{shed\_noncritical}$ để ép thuật toán dồn mọi tài nguyên cứu Bệnh viện/Trạm phát sóng. Nới lỏng điện áp xuống $0.90$ p.u.
- **💻 Triển khai Mã nguồn (`Function.py`):**
  - Viết mới `object_function()` để Tối thiểu hóa Cắt tải (Minimize Load Shedding).
  - Khai sinh các biến vật lý: `P_shed_critical`, `P_shed_noncritical`.
  - Cập nhật phương trình cân bằng Vô công (Q-balance): Thêm `Q_shed` và máy phát bù `Q_DG` để chống sụp đổ điện áp.


## Slide 5: [Temporal Level] MPC và Cỗ máy thời gian 3 Pha
- **Lý thuyết:** Lịch Day-Ahead tĩnh bị vô hiệu hóa khi đứt gãy. MPC quản trị rủi ro qua 3 pha:
  1. **Pre-fault:** Quỹ đạo Day-ahead tĩnh.
  2. **Emergency (Rolling Horizon):** Chạy lùi từng giờ. Dùng *End-of-horizon SOC penalty* để ngăn BESS xả kiệt pin thiển cận.
  3. **Post-fault:** Cập nhật $SOC_{actual}$ còn lại để sinh lịch Day-ahead khôi phục.
- **💻 Triển khai Mã nguồn (`build_model.py`):**
  - Hàm `run_MPC_simulation()` điều phối vòng lặp và truyền lượng Pin gối đầu.
  - Hàm `apply_fault()` đánh sập dòng/nguồn theo biến thời gian thực $t$.

## Slide 6: [Execution] Đề xuất Kịch bản Stress-Testing
- **Lý thuyết:** "Dồn thảm họa vào nhóm yếu (MG1, MG2 tải nặng) - Ép nhóm mạnh (MG3, MG4 Renewable/Diesel) ứng cứu".
- **4 Kịch bản (Cần GVHD chốt):** (1) Islanded, (2) Đứt cáp Tie-line, (3) Mất điện mặt trời (Solar), (4) Thảm họa kép N-2.
- **💻 Triển khai Mã nguồn (`main.py`):**
  - Sử dụng mảng linh hoạt `fault_configs` (Dictionary) quy định chính xác `start_time`, `end_time`, `fault_type` cho từng vị trí để giả lập thảm họa đồng thời.

## Slide 7: Live Demo & Kế hoạch tiếp theo (Next Steps)
- **Live Demo:** Chuyển sang màn hình VSCode, show tiến trình chạy mượt mà của `run_MPC_simulation()`.
- **Kế hoạch Tuần (Sprint 3 & 4):** Trích xuất Data từ 4 kịch bản này để vẽ biểu đồ so sánh 24h sắc nét và bắt đầu viết bài báo học thuật.

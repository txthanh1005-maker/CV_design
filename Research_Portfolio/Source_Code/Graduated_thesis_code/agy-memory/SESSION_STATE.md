## Goal
Tổng hợp và duy trì toàn bộ bộ nhớ dự án P2P_trading_withQV_MG1234 (đã gộp từ _AI_Memory_Bank cũ) để đóng vai trò là "Supreme Source of Truth" quản lý toàn bộ vòng đời của hệ thống. Chuẩn bị cho báo cáo Thuyết trình (Top-Down Presentation Report).

## Constraints
- Tuyệt đối tuân thủ kiến trúc hệ thống hiện tại: Hierarchical ATC, thuật toán MPC & SOCP.
- Không tự ý sửa đổi code lõi (`main.py`, `build_model.py`, v.v.), trừ khi có lỗi hoặc yêu cầu thêm kịch bản mới.
- Quản lý bộ nhớ hoàn toàn thông qua thư mục `agy-memory/` theo chuẩn mới.

## Progress & Changelog
**Giai đoạn trước:** Đã gộp và hợp nhất hệ thống (Refactoring sang Real-time MPC, sửa lỗi Voltage Collapse bằng `Q_shed` và phạt lạnh khởi động, chuyển ADMM sang ATC).
**Mới nhất (Hoàn thành Task 1 & Task 2.1):**
- **Hoàn tất Khảo sát Tài liệu (Literature Review):** Đánh giá 2 phương pháp phân bổ Tải quan trọng và chọn phương án 20% công suất mỗi node.
- **Hoàn tất Kịch bản Lỗi (Động lực học sự cố):** Chọn Kịch bản N-2 Dây chuyền (Cascading RE Drop + Grid Loss) đánh vào nhóm nhỏ (MG1, MG2) để tạo áp lực chênh lệch công suất, phô diễn sức mạnh phân bổ P2P.
- **Hoàn tất Task 1 (Stress-Test Code):** Sửa lỗi định danh biến điện gió trong `Function.py`, cập nhật `main.py` với cấu hình sự cố mới. Thuật toán MPC đã chạy thành công rực rỡ, hội tụ toàn bộ các khung giờ trong pha khẩn cấp (từ 12 đến 23) mà không văng lỗi Infeasible.
- **Hoàn tất Task 2.1 (IEEE Research on Visualizations and Base Cases):** [EMPHASIS: BUILD ONLY] Hoàn thành nghiên cứu tài liệu chuẩn IEEE. Đã chạy thành công extreme stress-tests (Kịch bản Cascading PV/Grid drop ở những giờ có lượng năng lượng tái tạo - RE cao). Mô hình được build thành công rực rỡ và chạy hoàn hảo qua các giới hạn khắc nghiệt. Đã chốt được 2 Base Cases (Isolated Mode, Perfect Foresight) và 4 loại đồ thị chuẩn (SOC, P2P Flow, Load Shedding, Convergence Tracking).
- **Hoàn tất Task 2 (Warm-Start Algorithmic Optimization):** Đã nhúng Hybrid Warm-Start (dùng Day-Ahead cho giờ đầu sự cố, dùng kết quả t-1 cho các giờ tiếp theo) và Adaptive Initial Rho (nâng hệ số rho khởi tạo lên 0.5) vào vòng lặp MPC trong `build_model.py` và `main.py`. Code đã pass qua Test Engineer, giúp khắc phục triệt để tình trạng hội tụ chậm do hàm phạt cắt tải (Penalty = 500,000) gây ra.

- **Hoàn tất Task 3.2 (Data Export & Plotting):** Lập trình trích xuất dữ liệu Gurobi/IPOPT và tạo 3 đồ thị IEEE (P2P Power Flow, BESS SOC, Load Shedding) qua Matplotlib, lưu dưới dạng PNG độ phân giải cao tại `Result_data/`. Test Engineer đã sửa lỗi memory leak (thiếu plt.close) và lỗi định dạng array.
- **Bổ sung tính năng giám sát lỗi vô nghiệm (Infeasible Monitoring):** Đã nhúng cơ chế tự động kiểm tra kết quả giải của từng MG trong vòng lặp ATC của MPC (`build_model.py`). Nếu xảy ra vô nghiệm, hệ thống sẽ tự động in log chi tiết các ràng buộc vi phạm và kích hoạt dừng khẩn cấp mô phỏng MPC. Chạy thử nghiệm thực tế thành công tốt đẹp.

## Key Decisions
1. **Sử dụng ATC thay cho ADMM:** Đảm bảo quyền riêng tư và tốc độ hội tụ nhanh qua Virtual P2P Market Hub.
2. **Sử dụng MPC Rolling Horizon:** Đảm bảo "Risk Awareness" cập nhật thực tế liên tục trong pha khẩn cấp. 
3. **SOCP Relaxation:** Đảm bảo bài toán lồi, tối ưu toàn cục đáng tin cậy.
4. **Soft Penalty cho Resilience:** Phạt kinh tế lớn thay vì ràng buộc cứng đối với Tải quan trọng để tránh lỗi Infeasible.
5. **Phân bổ tải quan trọng:** Ấn định **20% công suất tại mỗi node** thay vì chọn 20% số lượng node, nhằm tối đa hóa độ trơn tru (smoothness) của biểu đồ điện áp và hỗ trợ SOCP.
6. **Stress Testing (N-2 Contingencies):** Dựa trên cấu trúc 4 MG có tỷ lệ RE cao, kịch bản lỗi sẽ tập trung vào sự kiện HILP nghiêm trọng như mất kết nối lưới chính đồng thời với **sụt giảm cực đoan Năng lượng tái tạo (RE drop)** do thời tiết xấu. Kịch bản này làm nổi bật vai trò dự phòng thiết yếu của DG (buộc khởi động khẩn cấp từ trạng thái tắt) và ép MPC đạt giới hạn trong việc phân phối lại năng lượng để cứu tải quan trọng.
7. **Động lực học Sự cố (Fault Dynamics):** Áp dụng sự cố lên 1 hoặc 2 MG (Subset Faults) theo tiến trình dây chuyền (Cascading). Thiết lập này tạo chênh lệch công suất ép các MG phải giao dịch P2P, đồng thời chứng minh sức mạnh dự báo và phản ứng thời gian thực của thuật toán MPC Rolling-horizon so với mô hình tĩnh.
8. **Base Cases & Visualizations:** Dựa trên chuẩn IEEE, chốt 2 Base Cases ("Isolated Mode" và "Perfect Foresight") và 4 đồ thị hiển thị (SOC, P2P Flow, Load Shedding, Convergence Tracking) để đánh giá thuật toán.
9. **Tối ưu tốc độ hội tụ (Warm-Start & Adaptive Rho):** Áp dụng Hybrid Warm-Start (Day-Ahead cho t_fault, t-1 cho t>t_fault) kết hợp với Adaptive Initial Rho để giảm số vòng lặp khi giá điện P2P phải leo thang từ 0 để đối chọi với hàm phạt cắt tải (Penalty = 500,000).

## Next Steps
- Bắt đầu tiến hành **Task 4 (Chạy Benchmark Perfect Foresight)** để lấy số liệu so sánh (Optimality Gap) làm cơ sở chứng minh hiệu năng của Hybrid Warm-Start MPC.
- Cuối cùng tiến hành **Task 5 (Viết Báo cáo)** để tổng hợp và xuất bản Draft 1.

## Critical Context
**Cấu hình mạng (Topology):** 1 Main Grid (MG0) & 4 Microgrids.
- **MG1 (Nặng tải, 36 nodes):** Tải ~6266 kWh/day, có PV, Wind, DG, BESS. Liên kết MG4, MG3.
- **MG2 (Solar-only, 30 nodes):** Tải ~5847 kWh/day, có PV, DG, BESS. Liên kết MG3, MG4.
- **MG3 (Nhẹ tải/Dư thừa, 21 nodes):** Đóng vai trò cứu tinh. Tải ~2458 kWh/day, PV, Wind. Liên kết MG1, MG2, MG4.
- **MG4 (Máy phát mạnh, 35 nodes):** Tải ~5433 kWh/day, có PV, 2 DGs, BESS. Đóng vai trò cứu tinh dự phòng khẩn cấp.
**Cơ chế hoạt động kép:**
- *Day-ahead Scheduling:* Tối ưu hóa lợi ích kinh tế (24h).
- *Emergency MPC:* Chạy cuốn (rolling) từng giờ, kích hoạt cơ chế cách ly lỗi, bù phản kháng, và chia sẻ P2P.

## Folder Structure Summary
Sơ đồ phân bổ dữ liệu và mã nguồn:
- **Tài liệu đặc tả và Memory**:
  - `0_System_Specs/`: Các tài liệu đặc tả ban đầu.
  - `agy-memory/`: Thư mục điều khiển bộ nhớ (Mới, là Supreme Source of Truth).
  - `workspace/`: Nơi chứa kết quả công việc đang tiến hành (`Idea.md`, `ACTION_PLAN.md`, báo cáo).
- **Dữ liệu đầu vào (Input Data)**:
  - `Line_data/`, `Node_PQ_data/`: Cấu trúc vật lý của các Microgrid.
  - `Source_data/`, `Trading_data/`: Dữ liệu phát điện và giao dịch ngang hàng (P2P).
  - `Result_data/`: Nơi xuất kết quả chạy mô phỏng.
- **Mã nguồn (Core Scripts)**:
  - `main.py`: Entry point điều khiển luồng kịch bản (khởi tạo, Day-ahead, Emergency loop, fault scenarios).
  - `build_model.py`: Chứa các module xây dựng mô hình (`ATC_Global_model()`, chạy mô phỏng `run_MPC_simulation()`, bơm sự cố `apply_fault()`).
  - `Function.py`: Triển khai các ràng buộc vật lý, nới lỏng SOCP, `Q_shed`, và hàm phạt (Augmented Lagrangian).
  - `Function_maingrid.py`: Quản lý vòng lặp cấp lưới chính (DSO/Coordinator).

## Asset Pointers
- `D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\workspace\Idea.md`
- `D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\workspace\ACTION_PLAN.md`
- `D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\workspace\Presentation_Report.md`
- `D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\agy-memory\SESSION_STATE.md`

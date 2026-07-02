# TỔNG HỢP KỊCH BẢN SỰ CỐ VÀ PHÂN BỔ PHỤ TẢI QUAN TRỌNG
*(Cập nhật từ phiên làm việc ngày 03/06/2026)*

Tài liệu này tổng hợp các kết quả nghiên cứu (được giới hạn độc quyền từ IEEE Xplore và ScienceDirect) liên quan đến Kịch bản sự cố (Fault Scenarios) và Vị trí Phụ tải quan trọng (Critical Load Placement) áp dụng cho hệ thống 4 Microgrids.

---

## 1. PHÂN LOẠI VÀ THIẾT LẬP KỊCH BẢN SỰ CỐ (STRESS-TESTING SCENARIOS)

Qua nghiên cứu học thuật, các sự cố điện vật lý được phân loại và thiết lập thành 4 kịch bản kiểm thử độ chịu lỗi (Resilience Stress-Testing) với mức độ nghiêm trọng tăng dần:

### 1.1. Phân loại sự cố cốt lõi
1. **Mất nguồn cấp chính (Main Grid Blackout):** Chuyển đổi trạng thái hệ thống từ nối lưới sang độc lập (Islanded Mode).
2. **Đứt đường dây liên kết P2P (Tie-line Fault):** Chia cắt một phần mạng lưới, ép các MGs phải tìm đường truyền tải phụ hoặc tự cân bằng.
3. **Hỏng nguồn phát phân tán cục bộ (DER Failure):** Gây thiếu hụt công suất đột ngột, đòi hỏi sự hỗ trợ chéo khẩn cấp từ các MGs lân cận.

### 1.2. Đề xuất 4 Kịch bản áp dụng thực tế
- **Kịch bản 1 (Mất lưới chính):** $t=2$ đến $t=6$. Kiểm tra quá trình ngắt PCC và điều khiển tần số/điện áp nội bộ.
- **Kịch bản 2 (Đứt cáp Tie-line):** $t=8$ đến $t=10$. Đứt đường dây trọng yếu giữa MG1 và MG2. Đánh giá tính năng tái định tuyến và cô lập lỗi.
- **Kịch bản 3 (Mất DER nội bộ):** $t=14$ đến $t=17$. Toàn bộ nguồn phát tại MG3 ngừng hoạt động. Kiểm tra khả năng bơm công suất từ MG1, MG2, MG4 sang cứu viện MG3.
- **Kịch bản 4 (Thảm họa kép N-2):** $t=19$ đến $t=24$. Vừa mất lưới chính, vừa đứt tie-line chia cắt cụm (MG1, MG2) khỏi cụm (MG3, MG4). Đánh giá tính năng phân cụm độc lập (Clustering survivability).

---

## 2. CHUẨN MỰC VÀ PHÂN BỔ PHỤ TẢI QUAN TRỌNG (CRITICAL LOAD PLACEMENT)

Hệ thống MPC yêu cầu bảo vệ tuyệt đối các Phụ tải Quan trọng (Critical Loads - không được phép Load Shedding). Các tiêu chuẩn lựa chọn được rút ra từ tài liệu khoa học:

### 2.1. Benchmark học thuật
- **Tỷ lệ phần trăm (%):** Mức 10% - 20% dung lượng phụ tải được coi là chuẩn mực tối ưu để đảm bảo khả năng sinh tồn (Tier 1 & Tier 2) mà không làm cạn kiệt quá nhanh nguồn dự trữ (BESS).
- **Tiêu chí Vị trí:** Phụ tải quan trọng phải được đặt gần hoặc tích hợp chung Node với các nguồn DER, BESS. Việc này nhằm:
  - Giảm thiểu sụt áp (Voltage Sag) dọc đường dây.
  - Giảm hao phí truyền tải (Line Loss).
  - Đảm bảo tải vẫn sống sót ngay cả khi bị chia tách thành các đảo nhỏ nhất.

### 2.2. Phân bổ thực tế trên Topology 4 MGs
Dựa trên nguyên tắc ~20% tải và sát nguồn DER, các Node sau đã được gán cờ Critical Load:
- **MG1 (21.7% số tải):** `{4, 14, 19, 31, 36}` (VD: Node 19 chứa BESS, Node 31 sát Wind).
- **MG2 (21.7% số tải):** `{10, 14, 20, 28, 30}` (VD: Node 10 chứa DG, Node 20 chứa BESS).
- **MG3 (23.0% số tải):** `{8, 10, 13}` (VD: Node 13 sát BESS).
- **MG4 (20.0% số tải):** `{10, 18, 23, 27, 28}` (VD: Node 10 sát BESS, Node 23 & 28 sát DG).

Kết quả này cấu thành bộ thông số đầu vào chính thức để tiến hành lập trình kiểm thử mô phỏng sự cố (Inject Faults) trong pha tiếp theo.

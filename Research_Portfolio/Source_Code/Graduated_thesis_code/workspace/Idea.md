# Bản Đặc Tả Kế Hoạch (Idea) - Xây dựng quy trình Top-Down & Cập nhật trạng thái Code
*(Tạo bởi Meta-Agent / CEO)*

## 1. Mục tiêu (Objective)
- Chuẩn hóa quy trình vận hành và báo cáo của dự án theo cách tiếp cận **Top-Down** (Từ Lý thuyết Kiến trúc -> Luồng Thuật toán -> Chi tiết Mã nguồn).
- Kiểm tra, phân tích và tài liệu hóa chính xác **những gì mã nguồn hiện tại đang thực thi** (Luồng khởi chạy trong `main.py`, chế độ lỗi nào đang bật, MPC hay Day-Ahead đang chạy).

## 2. Đầu ra dự kiến (Expected Deliverables)
- **Tài liệu Top-Down Process:** Một file tổng hợp (hoặc sơ đồ) mô tả rõ ràng luồng chạy của chương trình từ lúc đọc dữ liệu -> Khởi tạo Day-ahead -> Bơm sự cố (Apply Fault) -> Chạy vòng lặp MPC -> Phục hồi. Rất hữu ích để trình bày cho Giảng viên hướng dẫn.
- **Báo cáo Trạng thái Code (Current Code State):** Quét qua các file `main.py`, `build_model.py`, `Function.py` để xác nhận chế độ nào (fault scenarios, solver settings) đang được Active.

## 3. Ranh giới Dự án (Boundaries & Scope)
- Đây là tác vụ thiên về **Phân tích (Analysis)** và **Tài liệu hóa (Documentation)**.
- Các Sub-Agent (Researcher, Code Generator) sẽ được ủy quyền đọc code, tổng hợp luồng và viết báo cáo.
- **Tuyệt đối KHÔNG** tự ý sửa đổi logic toán học hay cấu trúc file code lõi trong pha này. Chỉ Read & Report.

## 4. Các bước tiến hành sơ bộ (Action Steps)
1. Quét nội dung `main.py` để xem luồng khởi tạo (EntryPoint).
2. Quét nội dung `build_model.py` và `Function.py` để nắm cấu trúc hàm gọi (Calling Structure).
3. Tổng hợp thành tài liệu Top-Down.

## 5. Quyết định Kiến trúc & Kịch bản (Cập nhật từ Task 0)
- **Cấu hình Tải quan trọng (Critical Load):** Áp dụng mức **20% công suất tại mỗi node** (thay vì 20% số lượng node). Lựa chọn này giúp toán tử SOCP Relaxation và MPC hội tụ tốt hơn do biểu đồ điện áp trơn tru hơn.
- **Kịch bản Stress-Test:** Sử dụng **Kịch bản sự cố N-2** (Cắt lưới chính kết hợp đứt đường dây P2P, hoặc Cắt lưới chính kết hợp **sụt giảm cực đoan Năng lượng Tái tạo**). Do 4 MG có độ đâm xuyên RE cao và DG thường xuyên tắt ở base-case, kịch bản mất RE sẽ ép các DG phải khởi động khẩn cấp để cứu tải quan trọng, làm nổi bật vai trò sống còn của DG và năng lực điều phối của MPC.
- **Động lực học Sự cố (Fault Dynamics):** Sự cố sẽ được áp dụng lên một phần của hệ thống (VD: 1 hoặc 2 MG) để tạo chênh lệch công suất, ép các MG khỏe mạnh phải truyền tải điện năng P2P. Chuỗi sự kiện sẽ diễn ra theo kịch bản **dây chuyền (Cascading / Sequential)** để chứng minh khả năng tối ưu hóa động (Rolling-horizon) của MPC khi phải liên tục phản ứng với biến cố mới.
- **Tối ưu tốc độ hội tụ (Warm-Start & Adaptive Rho):** Để giải quyết vấn đề hội tụ chậm do chênh lệch khổng lồ giữa hàm phạt cắt tải (Penalty = 500,000) và tốc độ tăng của giá điện P2P (lamda từ 0, rho = 0.05), hệ thống áp dụng chiến lược:
  1. **Hybrid Warm-Start:** Giờ đầu sự cố ($t=t_{fault}$) dùng kết quả Day-Ahead làm điểm khởi tạo. Các giờ sau dùng kết quả của $t-1$.
  2. **Adaptive Initial Rho:** Tăng rho hoặc tăng hệ số nhân tau trong những vòng lặp đầu của pha khẩn cấp để giá điện lamda nhanh chóng phản ánh mức độ khan hiếm năng lượng.

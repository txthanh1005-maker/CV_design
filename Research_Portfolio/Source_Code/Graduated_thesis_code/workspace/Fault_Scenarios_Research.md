# Khảo sát Tài liệu: Các kịch bản sự cố Microgrid phục vụ Stress Test

## 1. Tổng quan và Mục đích
Độ bền bỉ (resilience) của Microgrid được đánh giá thông qua quá trình **stress test** — một phương pháp mô hình hóa dựa trên kịch bản nhằm đánh giá hiệu suất của hệ thống dưới tác động của các nhiễu loạn cường độ cao. Khác với quy hoạch độ tin cậy tiêu chuẩn (sự cố N-1), quy hoạch hướng tới độ bền bỉ thường đánh giá các **sự cố N-k** (với $k \ge 2$) để kiểm tra khả năng sinh tồn của hệ thống và sự tối ưu hóa quá trình cắt tải bằng Điều khiển Dự báo Mô hình (MPC).

## 2. Các loại sự cố tiêu chuẩn trong Y văn

Dựa trên khảo sát các cơ sở dữ liệu học thuật (OpenAlex/IEEE), dưới đây là các kịch bản sự cố tiêu chuẩn thường được sử dụng để stress test các microgrid:

### 2.1. Ngắt kết nối Lưới chính (Chế độ Tách đảo / Islanding)
*   **Mô tả:** Hệ thống bị buộc chuyển từ chế độ nối lưới sang chế độ hoạt động độc lập (tách đảo) do lỗi từ lưới điện chính.
*   **Tác động:** Microgrid phải dựa hoàn toàn vào các Nguồn năng lượng phân tán (DER) tại chỗ để duy trì nguồn điện cho các phụ tải quan trọng.
*   **Vai trò trong thử nghiệm:** Đây thường là **sự cố N-1** cơ sở. Nó kiểm tra khả năng cơ bản của MPC trong việc cân bằng cung cầu tại chỗ và kích hoạt quá trình cắt tải khẩn cấp nếu cần.

### 2.2. Sụt giảm Năng lượng Tái tạo đột ngột (RE Drop)
*   **Mô tả:** Đột ngột sụt giảm nghiêm trọng công suất từ các Nguồn năng lượng tái tạo (RE) như Quang năng (PV) hoặc Phong điện (do mây che phủ dày đặc hoặc bão).
*   **Tác động:** Tạo ra sự thâm hụt nghiêm trọng về nguồn cung ứng do hệ thống (trong điều kiện bình thường) phụ thuộc lớn vào năng lượng tái tạo.
*   **Vai trò trong thử nghiệm:** Ép hệ thống phải khởi động khẩn cấp các máy phát dự phòng (DG) vốn đang tắt trong chế độ cơ sở (base case). Qua đó, đánh giá chi phí khởi động và khả năng bù đắp của DG để duy trì độ ổn định của hệ thống.

### 2.3. Đứt đường dây P2P / Đường dây liên kết
*   **Mô tả:** Mất kết nối đường dây điện vật lý hoặc liên kết truyền thông giữa các microgrid đang liên kết với nhau.
*   **Tác động:** Ngăn cản việc chia sẻ công suất và giao dịch ngang hàng (P2P).
*   **Vai trò trong thử nghiệm:** Đánh giá độ bền bỉ của mạng lưới microgrid. Kiểm tra xem MPC phân tương có duy trì được tính khả thi khi không có sự hỗ trợ từ các đối tác bên ngoài hay không, qua đó tránh được sự sụp đổ dây chuyền.

### 2.4. Các sự kiện thời tiết cực đoan (Sự kiện HILP)
*   **Mô tả:** Các sự kiện có Tác động Cao, Xác suất Thấp (HILP) như bão tuyết hoặc siêu bão.
*   **Tác động:** Gây ra hàng loạt sự cố mất điện đồng thời và dây chuyền trên cả mạng lưới phát và phân phối điện (Sự cố N-k).
*   **Vai trò trong thử nghiệm:** Đánh giá "Tỷ lệ Sống sót" và chi phí cắt tải trong kịch bản tồi tệ nhất.

## 3. Các kịch bản được đề xuất cho Dự án MPC hiện tại

Để kiểm tra đầy đủ thuật toán MPC của dự án và chứng minh độ bền bỉ, chúng tôi đề xuất triển khai các kịch bản có tính trọng tâm sau:

1.  **Kịch bản A: Ngắt kết nối Lưới chính kéo dài (Giờ Cao điểm)**
    *   *Thiết lập:* Cắt kết nối với lưới điện chính (VD: đứt liên kết MG0 - Lưới chính) trong khung giờ cao điểm (VD: từ giờ thứ 12 đến 16).
    *   *Mục đích:* Kiểm tra khả năng sinh tồn cơ bản trong chế độ tách đảo và phản hồi sơ cấp của các biến bù trừ (slack variables) trong quá trình cắt tải.

2.  **Kịch bản B: Sự cố N-2 nghiêm trọng (Mất Lưới + Đứt dây P2P)**
    *   *Thiết lập:* Đồng thời mất kết nối lưới chính VÀ đứt một đường dây liên kết P2P quan trọng (VD: đứt MG0-MG1) trong lúc nhu cầu phụ tải cao.
    *   *Mục đích:* Tạo áp lực cực đại lên nguồn phát cục bộ của một MG bị cô lập. Đánh giá xem solver (Gurobi/IPOPT) của MPC có hội tụ tốt và khả thi khi không có sự hỗ trợ P2P hay không.

3.  **Kịch bản C: Khủng hoảng kép (Mất Lưới + Sụt giảm Năng lượng Tái tạo)**
    *   *Thiết lập:* Trong khi hệ thống đang tách đảo, bơm thêm lỗi sụt giảm 80-100% công suất năng lượng tái tạo (PV/Wind) do thời tiết cực đoan. Máy phát DG (vốn đang tắt) buộc phải khởi động nguội.
    *   *Mục đích:* Làm nổi bật vai trò sống còn của DG trong việc quản lý sự cố. Kiểm tra khả năng của MPC trong việc quyết định kích hoạt DG (tính toán chi phí khởi động) và phân bổ cắt tải khẩn cấp (C_shed) để cứu các tải quan trọng.

### 3.1 Động lực học Sự cố trong mạng lưới 4 MG

Trong bối cảnh mạng lưới 4 Microgrids (MG) với mức độ thâm nhập Năng lượng Tái tạo (RE) cao, việc thiết kế kịch bản sự cố (ví dụ: sụt giảm RE do thời tiết) cần tuân thủ hai nguyên tắc trọng tâm để làm nổi bật ưu điểm của thuật toán MPC phân tán và chia sẻ công suất P2P:

**1. Phạm vi sự cố: Nên tác động lên một phần của mạng lưới (Ví dụ: 1 hoặc 2 MG) thay vì toàn bộ 4 MG.**
*   *Lý do:* Nếu sự cố xóa sổ RE trên cả 4 MG cùng lúc, toàn bộ mạng lưới không còn điện dư thừa để chia sẻ, và mỗi MG sẽ buộc phải tự độc lập cắt tải. Ngược lại, nếu sự cố chỉ diễn ra cục bộ (VD: MG1 và MG2 mất PV), các MG khỏe mạnh (MG3 và MG4) vẫn sẽ duy trì được lượng công suất dư thừa. 
*   *Giá trị chứng minh:* Kịch bản này tạo ra sự chênh lệch cung-cầu trong mạng lưới, kích hoạt thuật toán Distributed MPC điều tiết dòng điện dư từ MG3, MG4 qua mạng P2P để "cứu trợ" MG1, MG2. Điều này minh chứng trực quan nhất cho độ bền bỉ (resilience) và sức mạnh tương hỗ của cơ chế P2P, giúp hạn chế tối đa việc cắt tải quan trọng.

**2. Tiến trình sự cố: Nên diễn ra liên tiếp/dây chuyền (Sequential/Cascading) thay vì đồng thời (Simultaneous).**
*   *Lý do:* Sự cố đồng thời chỉ yêu cầu thuật toán tính toán lại điểm cân bằng một lần. Tuy nhiên, nếu sự cố mang tính chất dây chuyền (VD: $t=10$ MG1 hỏng turbine gió, $t=20$ MG2 mất điện mặt trời), trạng thái mạng lưới sẽ liên tục thay đổi.
*   *Giá trị chứng minh:* Các sự kiện liên tiếp đặc biệt làm nổi bật tính năng "Rolling-horizon" (Tối ưu hóa đường chân trời cuộn) cốt lõi của MPC. Nó thể hiện rõ khả năng liên tục cập nhật dự báo, thích ứng động và tự động điều chỉnh cấu hình chia sẻ năng lượng P2P theo thời gian thực để ngăn chặn sự sụp đổ dây chuyền của lưới.


## 4. Kết luận
Đối với dự án này, việc áp dụng **Kịch bản B** hoặc **Kịch bản C** (các sự cố N-2) sẽ mang lại bài kiểm tra áp lực (stress-test) khắt khe nhất về mặt toán học. Nó sẽ đẩy các bộ giải Gurobi/IPOPT đến giới hạn lớn nhất, qua đó chứng minh tính cần thiết và hiệu quả tối ưu của MPC so với các mô hình tham chiếu lý tưởng (perfect foresight).

---
### Tài liệu tham khảo
1. Microgrid Resilience and Stress Testing Methodologies (Frontiers in Energy Research, MDPI).
2. N-k Contingency Planning and Survivability Rates in Networked Microgrids (IEEE / Energy Central).
3. Robust and Distributed Model Predictive Control for Microgrid Emergency Operation and Load Shedding (Science Direct).

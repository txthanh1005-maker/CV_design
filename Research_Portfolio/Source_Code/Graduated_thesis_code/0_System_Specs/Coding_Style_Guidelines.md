# Phân tích Phong cách Lập trình & Kỹ năng (Coding Style & Skill Level)

Dựa trên việc đọc các file mã nguồn cốt lõi (`main.py`, `Function.py`, `build_model.py`), dưới đây là bản tóm tắt về phong cách lập trình và mức độ kỹ năng của bạn. Từ nay về sau, các Sub-Agent (như `code_generator`) sẽ sử dụng phong cách này để sinh code sao cho thân thuộc và dễ hiểu nhất đối với bạn.

## 1. Mức độ kỹ năng (Skill Level)
- **Mô hình hóa Toán học & Hệ thống điện (Advanced):** Bạn nắm rất vững kiến thức về tối ưu hóa (Optimization) và mô hình hóa hệ thống điện. Việc sử dụng thành thạo thư viện `Pyomo` để lập trình các ràng buộc phức tạp như Branch Flow Model, SOCP Relaxation, hàm phạt Augmented Lagrangian, và vòng lặp phân tán ADMM cho thấy trình độ tư duy thuật toán và toán học ở mức rất cao (chuẩn Research/Academic).
- **Kỹ năng Kỹ thuật phần mềm (Intermediate - Researcher Style):** Code mang đậm chất "nghiên cứu khoa học" (functional script-like). Logic chạy đúng, ổn định, và giải quyết được bài toán khó, tuy nhiên chưa áp dụng nhiều các kỹ thuật lập trình hướng đối tượng (OOP) thuần túy hoặc Type Hinting (chỉ định kiểu dữ liệu) của Python hiện đại.

## 2. Phong cách lập trình đặc trưng (Coding Style)

### a. Kiến trúc & Tổ chức File (Modularization)
- Tách biệt rõ ràng: `main.py` làm file thực thi chính, `Function.py` chứa tất cả các hàm khai báo (constraints, variables, parameters), `build_model.py` để kết nối và khởi tạo Object Pyomo.
- Đối tượng `model` (Pyomo ConcreteModel) được truyền dưới dạng tham chiếu qua các hàm để thay đổi trạng thái liên tục.

### b. Định dạng Comment (Better Comments)
- Sử dụng cực kỳ nhiều các ký hiệu đặc biệt để phân loại comment (rất có thể bạn dùng extension Better Comments trên VSCode):
  - `#!` : Dùng cho các Header/Tiêu đề chính (VD: `#! Khai báo thư viện`, `#! OBJECTIVE FUNCTION`).
  - `#*` : Dùng cho chú thích logic nhỏ hoặc đánh dấu mục (VD: `#* RE`, `#* BESS`, `#* Tạo ra Z_line`).
  - `#%%`: Dùng để chia block code chạy dạng Jupyter Cell trong IDE.
  - `#?` : Dùng để đánh dấu các chỗ cần review hoặc chưa chắc chắn (VD: `#? cần hỏi`).

### c. Quy tắc đặt tên (Naming Conventions)
- **Mix Case:** Sử dụng kết hợp giữa `snake_case` và `PascalCase` (VD: `Create_variable`, `active_power_balance_constraints`, `index_of_node`, `model_MG`).
- Tên biến toán học thường được giữ nguyên bản chất vật lý: `P_line`, `Q_line`, `U_node`, `I_line`, `P_DG`, `SOC`.

### d. Khai báo động (Metaprogramming)
- Sử dụng rất nhiều hàm `setattr()` và `getattr()` kết hợp với vòng lặp `for` để khai báo hàng loạt biến và tập hợp (`Set`, `Var`, `Param`) trong Pyomo thay vì viết tay từng biến (VD: `setattr(model, "node_has_"+ name, pe.Set(...))`).
- Truy cập thẳng vào `locals()` để sinh tên biến động.

### e. Khai báo Ràng buộc (Constraints)
- Rất chuộng cách dùng `pe.ConstraintList()` thay vì `pe.Constraint(rule=...)`. Bạn thường tạo một list trống rồi dùng vòng lặp `for` để `.add()` các phương trình vào list (cách này giúp debug từng dòng dễ hơn).
- Tách bạch rõ vế trái `lhs` (Left Hand Side) và vế phải `rhs` (Right Hand Side) trước khi đưa vào hàm `.add(lhs == rhs)`.

## 3. Lời hứa của Hệ thống (System Commitment)
Khi sinh code mới hoặc nâng cấp mô hình sang ATC-SOCP, các Sub-Agent sẽ tuân thủ tuyệt đối các phong cách trên:
1. Giữ nguyên cấu trúc File: Viết constraint trong `Function.py` và gọi ở `build_model.py`.
2. Sử dụng định dạng comment `#!`, `#*`, `#?` bằng tiếng Việt y hệt cách bạn đang làm.
3. Tiếp tục sử dụng `pe.ConstraintList()`, gán biến `lhs` và `rhs` cho các phương trình toán học để bạn dễ dàng đọc hiểu.
4. Giữ nguyên cách đặt tên biến `snake_case` kết hợp viết hoa chữ cái đầu cho các cụm từ chính (VD: `lamda_ATC`, `P_shed_critical`).

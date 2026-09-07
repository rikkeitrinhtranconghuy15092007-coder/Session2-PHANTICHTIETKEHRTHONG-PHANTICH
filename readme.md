# BÁO CÁO THIẾT KẾ HỆ THỐNG RIKKEIMART
**Dự án:** RikkeiMart - Dịch vụ đi chợ mua hộ thực phẩm sạch
**Hạng mục:** Chuẩn hóa giao tiếp bằng UML & Xử lý ngoại lệ quy trình vận hành

---

## PHẦN 1: VAI TRÒ CỦA UML & BẢNG ĐỊNH HƯỚNG SƠ ĐỒ

### 1. Vai trò của UML trong việc xóa bỏ rào cản giao tiếp
Việc ứng dụng UML (Unified Modeling Language) đóng vai trò then chốt giúp BA (Business Analyst), Dev (Developer) và Tester có chung một ngôn ngữ kỹ thuật, đặc biệt trong kịch bản phức tạp như khi cửa hàng hết thực phẩm:
*   **Trực quan hóa luồng rẽ nhánh logic:** Thay vì diễn đạt luồng "hết hàng - đề xuất - chờ 3 phút" bằng văn bản dài dòng dễ gây hiểu lầm, UML chuẩn hóa bằng các hình khối (Decision node, Control flow) rõ ràng. Dev nhìn vào sẽ lập trình đúng luồng, Tester nhìn vào sẽ viết đủ Test Case cho các nhánh ngoại lệ.
*   **Xác định rõ ràng trách nhiệm của hệ thống và người dùng:** UML mô tả chính xác ai (Tài xế, Khách hàng) làm gì, và hệ thống tự động can thiệp vào thời điểm nào (ví dụ: ngắt mạch Timeout sau 3 phút). Điều này triệt tiêu các "vùng xám" trong requirement, giúp Dev không phải tự đoán ý BA.

### 2. Bảng định hướng danh mục sơ đồ UML đề xuất

| Nhóm Sơ đồ | Loại Sơ đồ UML | Mục đích cụ thể trong dự án RikkeiMart |
| :--- | :--- | :--- |
| **Sơ đồ Hành vi** (Behavioral) | **Use Case Diagram** | Liệt kê các tác nhân (Tài xế, Khách hàng, Hệ thống) và các chức năng họ được phép thực hiện (Ví dụ: "Đề xuất món thay thế", "Phản hồi đề xuất", "Tự động ngắt mạch do Timeout"). |
| **Sơ đồ Hành vi** (Behavioral) | **Activity Diagram** | Mô tả chi tiết từng bước luồng nghiệp vụ khi Tài xế đến cửa hàng bị hết món. Đặc tả rõ nút rẽ nhánh (Decision) khi Khách hàng đồng ý, từ chối, và luồng đếm ngược 3 phút (Timer) dẫn đến hành động Auto-cancel. |
| **Sơ đồ Cấu trúc** (Structural) | **Class Diagram** | Định nghĩa các thực thể dữ liệu cần thiết để lập trình: `Order` (Đơn hàng), `OrderItem` (Món hàng), `ItemStatus` (Trạng thái). Sơ đồ chỉ rõ thuộc tính lưu vết sự thay đổi (món gốc -> món thay thế) và các phương thức như `processReplacement()`, `triggerTimeout()`. |

---
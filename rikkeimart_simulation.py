class CustomerTimeoutException(Exception):
    """Ngoại lệ tùy chỉnh để xử lý bẫy mất liên lạc (Unreachable Customer Trap)."""
    pass

def process_rikkeimart_order(item_status, customer_response):
    print(f"\n[RikkeiMart] Bắt đầu xử lý đơn hàng. Trạng thái món: {item_status.upper()}")
    try:
        if item_status == "in_stock":
            print("-> Hàng có sẵn. Tài xế lấy hàng và đi giao.")
            return "SUCCESS: Giao hàng bình thường."
        
        elif item_status == "out_of_stock":
            print("-> Hệ thống: Cửa hàng hết hàng. Tài xế chọn [Đề xuất sản phẩm thay thế tương đương].")
            print("-> Hệ thống: Gửi thông báo đến App Khách hàng. Bắt đầu bộ đếm Timeout 3 phút...")
            
            # Xử lý phản hồi của khách hàng và bẫy Timeout
            if customer_response == "timeout":
                raise CustomerTimeoutException("Quá 3 phút không nhận được phản hồi từ Khách hàng.")
            elif customer_response == "approve":
                print("-> Khách hàng: ĐỒNG Ý đổi món.")
                print("-> Hệ thống: Cập nhật món mới. Tài xế tiếp tục đi giao.")
                return "SUCCESS: Đã giao món thay thế."
            elif customer_response == "reject":
                print("-> Khách hàng: TỪ CHỐI đổi món.")
                print("-> Hệ thống: Tiến hành hủy đơn an toàn để giải phóng Tài xế.")
                return "CANCELLED: Khách từ chối."
            else:
                print("-> Hệ thống: Tín hiệu phản hồi không hợp lệ.")
                return "ERROR: Invalid response."

    except CustomerTimeoutException as e:
        print(f"[NGOẠI LỆ TIMEOUT] {e}")
        print("-> HỆ THỐNG XỬ LÝ (Auto-cancel): Tự động ngắt mạch, hủy đơn an toàn để giải phóng Tài xế.")
        return "CANCELLED_AUTO: Hủy do Timeout 3 phút."
    except Exception as e:
        print(f"[LỖI HỆ THỐNG] Lỗi không mong muốn xảy ra: {e}")
        return "ERROR: System Crash."

# --- CHẠY THỬ NGHIỆM MÔ PHỎNG CÁC KỊCH BẢN ---
if __name__ == "__main__":
    # 1. Kịch bản Suôn sẻ: Có hàng
    process_rikkeimart_order(item_status="in_stock", customer_response=None)
    
    # 2. Kịch bản Đổi món: Khách đồng ý
    process_rikkeimart_order(item_status="out_of_stock", customer_response="approve")
    
    # 3. Kịch bản Bẫy Edge Case: Khách tắt máy (Timeout 3 phút)
    process_rikkeimart_order(item_status="out_of_stock", customer_response="timeout")
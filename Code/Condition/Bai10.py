"""
    Câu 1: Tính Tiền Điện Theo Bậc Thang
    Công ty điện lực tính tiền điện theo bậc thang.
    Một chương trình cần tính hóa đơn điện cho một hộ gia đình.
    Thực hiện các yêu cầu sau:
    1. Cho người dùng nhập vào chỉ số điện năng tiêu thụ trong tháng
        (kWh, dạng số nguyên, giả sử kWh > 0).
    2. Áp dụng công thức tính tiền điện theo bậc thang sau
    [(giả sử đơn giá đã bao gồm VAT):
    • Bậc 1: 0 đến 50 kWh: 1.800 VNĐ/kWh
    • Bậc 2: 51 đến 100 kWh: 2.000 VNĐ/kWh
    • Bậc 3: 101 kWh trở lên: 2.500 VNĐ/kWh
    3. Xác định tổng số tiền phải trả dựa trên số kWh đã nhập.
    4. In ra tổng số tiền phải trả
"""

# Khai báo và nhập chỉ số điện
kWh = int(input("Nhập số điện tiêu thụ: "))
# Tính tiền điện
if kWh < 0:
    print("Giá trị không đúng")
elif kWh <= 50:
    tong_tien = kWh * 1800
    print(f"Tổng tiền điện: {tong_tien}")
elif kWh <= 100:
    tong_tien = 50 * 1800 + (kWh - 50) * 2000
    print(f"Tổng tiền điện: {tong_tien}")
else:
    tong_tien = 50 * 1800 + 50 * 2000 + (kWh - 100) * 2500
    print(f"Tổng tiền điện: {tong_tien}")
    
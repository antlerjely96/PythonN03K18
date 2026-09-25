# Nhập 2 số thực từ bàn phím. Tính +, -, *, / của 2 số

# Khai báo a, b
a = None
b = None
# Nhập a, b
a = float(input("a = "))
b = float(input("b = "))
# Tính +, -, *, /
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
# Hiển thị kết quả
print(f"a + b = {tong}")
print(f"a - b = {hieu}")
print(f"a * b = {tich}")
print(f"a / b = {thuong}")
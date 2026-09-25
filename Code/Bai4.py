# Nhập 2 số nguyên từ bàn phím. Tính +, -, *, /, %, //, ** của 2 số

# Khai báo a, b
a = None
b = None
# Nhập a, b
a = int(input("a = "))
b = int(input("b = "))
# Tính +, -, *, /
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
so_du = a % b
phan_nguyen = a // b
luy_thua = a ** b
# Hiển thị kết quả
print(f"a + b = {tong}")
print(f"a - b = {hieu}")
print(f"a * b = {tich}")
print(f"a / b = {thuong}")
print(f"a / b = {so_du}")
print(f"a / b = {phan_nguyen}")
print(f"a / b = {luy_thua}")
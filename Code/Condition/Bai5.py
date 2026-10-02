"""
    Nhap 3 so nguyen a, b, c. Hien thi so lon nhat va so nho nhat trong 3 so
"""

# Khai báo và nhập a, b, c
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
# Kiểm tra số lớn nhất
if a > b:
    if a > c:
        print(f"Số lớn nhất: {a}")
    else:
        print(f"Số lớn nhất: {c}")
else:
    if b > c:
        print(f"Số lớn nhất: {b}")
    else:
        print(f"Số lớn nhất: {c}")
# Kiểm tra số nhỏ nhất
if a < b:
    if a < c:
        print(f"Số nhỏ nhất: {a}")
    else:
        print(f"Số nhỏ nhất: {c}")
else:
    if b < c:
        print(f"Số nhỏ nhất: {b}")
    else:
        print(f"Số nhỏ nhất: {c}")
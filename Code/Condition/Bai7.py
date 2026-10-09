"""
    Nhap 3 so thuc tu ban phim.
    Kiem tra 3 so do co phai canh cua 1 tam giac hay khong
"""

# Khai báo và nhập 3 số thực
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
# Kiểm tra
if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        print("a, b, c tạo thành tam giác")
    else:
        print("a, b, c không tạo thành tam giác")
else:
    print("a, b, c không tạo thành tam giác")
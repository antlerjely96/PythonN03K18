"""
    1. Nhập 2 số nguyên a, b. Tính +, -, *, / của 2 số và hiển thị kết quả
    
    Note: Xác định số lượng hàm
    => Xác định số lượng chức năng (số việc phải làm) + main()
    => Xác định các hàm có tham số truyền vào không (xác định hàm có cần đầu vào để xử lý không)
    => Xác định các hàm có return không (xác định giá trị sau khi hàm chạy xong có cần dùng nữa không)
"""

# Nhập số => Không có tham số, có return
def nhap():
    a = int(input())
    return a

# Tính + => 2 tham số, có return
def tinhTong(a, b):
    tong = a + b
    return tong

# Tính - => 2 tham số, có return
def tinhHieu(x, y):
    hieu = x - y
    return hieu

# Tính * => 2 tham số, có return
def tinhTich(m, n):
    tich = m * n
    return tich

# Tính / => 2 tham số, có return
def tinhThuong(a, b):
    if b != 0:
        thuong = a / b
        return thuong
    else:
        return "Khong tinh duoc!"

# Hiển thị kết quả => 4 tham số, không có return
def hienThiKetQua(tong, hieu, tich, thuong):
    print(f"a + b = {tong}")
    print(f"a - b = {hieu}")
    print(f"a * b = {tich}")
    print(f"a / b = {thuong}")
    
# main() => không tham số, không return
def main():
    print("Nhap a:", end = " ")
    a = nhap()
    print("Nhap b:", end = " ")
    b = nhap()
    tong = tinhTong(a, b)
    hieu = tinhHieu(a, b)
    tich = tinhTich(a, b)
    thuong = tinhThuong(a, b)
    hienThiKetQua(tong, hieu, tich, thuong)

# Gọi main
if __name__ == "__main__":
    main()
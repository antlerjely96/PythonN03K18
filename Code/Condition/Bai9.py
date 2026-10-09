"""
    Nhập 1 số nguyên là tháng trong năm. Hiển thị số ngày của tháng đó
"""

# Khai báo và nhập tháng
thang = int(input("Nhập tháng: "))
# Lựa chọn
match thang:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f"Tháng {thang} có 31 ngày")
    case 4 | 6 | 9 | 11:
        print(f"Tháng {thang} có 30 ngày")
    case 2:
        # Khai báo và nhập năm
        nam = int(input("Nhập năm: "))
        # Kiểm tra năm
        if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
            print(f"Tháng {thang} có 29 ngày")
        else:
            print(f"Tháng {thang} có 28 ngày")
    case _:
        print("Không xác định")
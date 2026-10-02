"""
    Nhap thang la 1 so nguyen. Hien thi so ngay trong thang do.
    Nếu tháng là 2 thì cho nhập năm để xét tháng 2 năm đó có bao nhiêu ngày
"""

# Khai báo và nhập tháng
thang = int(input("Nhập tháng: "))
# Kiểm tra tháng
if thang <= 0 or thang > 12:
    print("Nhập sai")
elif thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    print(f"Tháng {thang} có 31 ngày")
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    print(f"Tháng {thang} có 30 ngày")
else:
    # Khai báo và nhập năm
    nam = int(input("Nhập năm: "))
    # Kiểm tra năm
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        print(f"Tháng {thang} năm {nam} có 29 ngày")
    else:
        print(f"Tháng {thang} năm {nam} có 28 ngày")
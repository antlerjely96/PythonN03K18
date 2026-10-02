"""
    Nhap so tuoi cua 1 nguoi tu ban phim (tuoi la so nguyen)
    Kiem tra:
        Neu tuoi > 0 and tuoi < 6: hoc mau giao
        Neu tuoi >= 6 and tuoi < 11: hoc cap 1
        Neu tuoi >= 11 and tuoi < 16: hoc cap 2
        Neu tuoi >= 16 and tuoi < 18: hoc cap 3
        Neu tuoi >= 18 and tuoi < 23: Hoc dai hoc
        Neu tuoi >= 23 and tuoi <= 65: Di lam
        Con lai: Nghi huu
"""

# Khai báo và nhập tuoi
tuoi = int(input("Nhập tuổi: "))
# Kiểm tra tuổi
if tuoi <= 0:
    print("Nhập sai")
elif tuoi < 6:
    print("Học mẫu giáo")
elif tuoi < 11:
    print("Học cấp 1")
elif tuoi < 16:
    print("Học cấp 2")
elif tuoi < 18:
    print("Học cấp 3")
elif tuoi < 23:
    print("Học cao đẳng hoặc đại học")
elif tuoi <= 65:
    print("Đi làm")
else:
    print("Nghỉ hưu")
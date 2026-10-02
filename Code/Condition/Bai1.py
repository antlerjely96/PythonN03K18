"""
    Nhập số nguyên a từ bàn phím. Kiểm tra a la số âm hay dương.
    Nếu a là số dương thì kiểm tra a là số chẵn hay lẻ
"""

# Khai báo và nhập a
a = int(input("a = "))
# Kiểm tra a
if a > 0:
    if a % 2 == 0:
        print(f"{a} là số chẵn")
    else:
        print(f"{a} là số lẻ")
elif a < 0:
    print(f"{a} là số âm")
else:
    print(f"{a} là số không âm không dương")
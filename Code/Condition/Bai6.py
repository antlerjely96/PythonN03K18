"""
    Nhập 3 số nguyên a, b, c. Tìm số nghiệm của phương trình a * x ** 2 + b * x + c = 0
"""

# Khai báo và nhập a, b, c
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
# Kiểm tra a == 0
if a == 0:
    # Kiểm tra b == 0
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình có 1 nghiệm")
else:
    # Tính delta
    delta = b ** 2 - 4 * a * c
    # Kiểm tra delta
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print("Phương trình có 1 nghiệm kép")
    else:
        print("Phương trình vô nghiệm")
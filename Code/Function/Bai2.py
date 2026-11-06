"""
    2. Nhập 1 số nguyên x. Kiểm tra x là số dương hay số âm
"""

def nhap():
    a = int(input())
    return a

def kiemTra(x):
    if x < 0:
        print(f"{x} la so am")
    elif x > 0:
        print(f"{x} la so duong")
    else:
        print(f"{x} la so khong am khong duong")

def main():
    print("x = ", end = "")
    x = nhap()
    kiemTra(x)
    
if __name__ == "__main__":
    main()
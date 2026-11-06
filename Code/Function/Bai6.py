"""
    6. Nhập 3 số nguyên a, b, c. Tìm số nghiệm của phương trình a * x ** 2 + b * x + c = 0
"""

def nhap():
    a = int(input())
    return a

def timSoNghiem(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "vo so"
            else:
                return 0
        else:
            return 1
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return 0
        elif delta == 0:
            return 1
        else:
            return 2

def main():
    print("a = ", end = "")
    a = nhap()
    print("b = ", end = "")
    b = nhap()
    print("c = ", end = "")
    c = nhap()
    print(f"Phuong trinh co {timSoNghiem(a, b, c)} nghiem")

if __name__ == "__main__":
    main()
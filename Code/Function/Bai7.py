"""
    7. Nhap 3 so thuc tu ban phim. Kiem tra 3 so do co phai canh cua 1 tam giac hay khong
"""

def nhap():
    a = float(input())
    return a

def kiemTra(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            return "co"
        else:
            return "khong"
    else:
        return "khong"
    
def main():
    print("a = ", end = "")
    a = nhap()
    print("b = ", end = "")
    b = nhap()
    print("c = ", end = "")
    c = nhap()
    print(f"{a}, {b}, {c} {kiemTra(a, b, c)} tao thanh tam giac")

if __name__ == "__main__":
    main()
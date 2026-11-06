"""
    4. Nhap thang la 1 so nguyen. Hien thi so ngay trong thang do
"""

def nhap():
    a = int(input())
    return a

def tinhSoNgay(thang):
    match thang:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            print(f"Thang {thang} co 31 ngay")
        case 4 | 6 | 9 | 11:
            print(f"Thang {thang} co 30 ngay")
        case 2:
            print("Nhap nam: ", end = "")
            nam = nhap()
            if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
                print(f"Thang {thang} co 29 ngay")
            else:
                print(f"Thang {thang} co 28 ngay")

def main():
    print("Nhap thang: ", end = "")
    thang = nhap()
    tinhSoNgay(thang)
    
if __name__ == "__main__":
    main()
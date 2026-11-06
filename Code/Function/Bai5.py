"""
    5. Nhap 3 so nguyen a, b, c. Hien thi so lon nhat va so nho nhat trong 3 so
"""

def nhap():
    a = int(input())
    return a

def timMax(a, b, c):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    return max

def timMin(a, b, c):
    min = a
    if min > b:
        min = b
    if min > c:
        min = c
    return min

def main():
    print("a = ", end = "")
    a = nhap()
    print("b = ", end = "")
    b = nhap()
    print("c = ", end = "")
    c = nhap()
    max = timMax(a, b, c)
    print(f"max = {max}")
    min = timMin(a, b, c)
    print(f"min = {min}")

if __name__ == "__main__":
    main()
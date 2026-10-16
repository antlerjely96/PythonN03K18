"""
    5. Nhap so nguyen n tu ban phim.
    Tinh tong cac so chia het cho 3 hoac 7 trong khoang tu 1 den n
"""

n = int(input("n = "))
tong = 0
for i in range(1, n + 1):
    if i % 3 == 0 or i % 7 == 0:
        tong += i
print(f"Tổng các số chia hết cho 3 hoặc 7 trong khoảng 1 đến {n}: {tong}")
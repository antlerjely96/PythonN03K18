"""
    4. Nhap so nguyen n tu ban phim.
    Tinh n!
"""

n = int(input("n = "))
if n < 0:
    print(f"Không có {n}!")
else:
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *= i
    print(f"{n}! = {giai_thua}")
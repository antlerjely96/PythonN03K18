"""
    3. Nhap so nguyen n tu ban phim.
    Hien thi cac so chan trong khoang tu 1 den n
"""

n = int(input("n = "))
for i in range(1, n):
    if i % 2 == 0:
        print(f"{i}", end = "  ")
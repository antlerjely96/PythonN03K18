"""
    2. Nhap so nguyen n tu ban phim.
    Hien thi cac so tu 1 den n
    Note:
        range(stop): mặc định start = 0, step = 1
        range(start, stop): mặc định step = 1
"""

n = int(input("n = "))
for i in range(1, n):
    print(f"{i}", end = "  ")
"""
    1. In ra các số liên tiếp từ 1 đến 20
    Tham số 1: i = 1
    Tham số 2: i < 20
    Tham số 3: i = i + 1
"""
print("Dùng for")
for i in range(1, 20, 1):
    print(f"{i}", end = "  ")
    
print("")
print("Dùng while")
i = 1
while i < 20:
    print(f"{i}", end = "  ")
    i += 1
    
        
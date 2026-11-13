"""
    17. Ve hinh
    *
    * *
    * * *
    * * * *
    * * * * *
    18. Ve hinh
    * * * * *
    * * * *
    * * *
    * *
    *
    19. Ve hinh
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * * *
    * * * *
    * * *
    * *
    *
"""

def veHinhXuoi():
    for i in range(1, n + 1):
        print("*" * i)

def veHinhNguoc():
    for i in range(5, 0, -1):
        print("*" * i)

def main():
    print("17")
    veHinhXuoi()
    print("18")
    veHinhNguoc()
    print("19")
    veHinhXuoi()
    veHinhNguoc()
    
if __name__ == "__main__":
    main()
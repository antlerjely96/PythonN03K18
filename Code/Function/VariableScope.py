# Biến toàn cục (Global Variable)
a = 5

def function1():
    print("Function 1")
    # Biến cục bộ
    a = 6
    print(f"a = {a}")
    
def function2():
    print("Function 2")
    global a
    a = 7
    print(f"a = {a}")
    
def main():
    function1()
    print("---------------------")
    function2()
    print("---------------------")
    print("Function main")
    print(f"a = {a}")
    
if __name__ == "__main__":
    main()
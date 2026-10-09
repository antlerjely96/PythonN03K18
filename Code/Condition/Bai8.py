"""
    Nhập 1 số nguyên thể hiện thứ trong tuần. Hiển thị tên của thứ đó.
"""
# Khai báo và nhập thứ
thu = int(input("Nhập thứ: "))
# Lựa chọn
if thu == 2:
    print("Thứ hai")
elif thu == 3:
    print("Thứ ba")
elif thu == 4:
    print("Thứ tư")
elif thu == 5:
    print("Thứ năm")
elif thu == 6:
    print("Thứ sáu")
elif thu == 7:
    print("Thứ bảy")
elif thu == 8:
    print("Chủ nhật")
else:
    print("Không xác định")
    
match thu:
    case 2:
        print("Thứ hai")
    case 3:
        print("Thứ ba")
    case 4:
        print("Thứ tư")
    case 5:
        print("Thứ năm")
    case 6:
        print("Thứ sáu")
    case 7:
        print("Thứ bảy")
    case 8:
        print("Chủ nhật")
    case _:
        print("Không xác định")
# ------------------------------------------------      
match thu:
    case 2:
        print("Ngày trong tuần")
    case 3:
        print("Ngày trong tuần")
    case 4:
        print("Ngày trong tuần")
    case 5:
        print("Ngày trong tuần")
    case 6:
        print("Ngày trong tuần")
    case 7:
        print("Cuối tuần")
    case 8:
        print("Cuối tuần")
    case _:
        print("Không xác định")
        
match thu:
    case 2 | 3 | 4 | 5 | 6:
        print("Ngày trong tuần")
    case 7 | 8:
        print("Cuối tuần")
    case _:
        print("Không xác định")
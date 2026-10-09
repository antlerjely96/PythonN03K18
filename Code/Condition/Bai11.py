"""
    Câu 2: Một công ty cần tính tổng số giờ làm việc thực tế của một nhân viên trong 4 tuần
    Thực hiện yêu cầu:
    1. Trong mỗi tuần, yêu cầu người dùng nhập số giờ làm việc thực tế
    trong 4 tuần gần nhất (dạng số thực float).
    2. Số giờ làm việc tiêu chuẩn mỗi tuần là 40 giờ. Kiểm tra và tính toán:
    • Tổng số giờ làm việc thực tế trong 4 tuần.
    • Tổng số giờ làm thêm (số giờ vượt quá 40 giờ trong mỗi tuần).
    • Tổng số giờ nghỉ (số giờ thiếu so với 40 giờ trong mỗi tuần).
    3. In ra Tổng số giờ làm việc thực tế,
    Tổng số giờ làm thêm, Tổng số giờ nghỉ của nhân viên.
"""

# Khai báo và nhập số giờ của 4 tuần
tuan_1 = float(input("Tuần 1: "))
tuan_2 = float(input("Tuần 2: "))
tuan_3 = float(input("Tuần 3: "))
tuan_4 = float(input("Tuần 4: "))
if tuan_1 > 0 and tuan_2 > 0 and tuan_3 > 0 and tuan_4 > 0:
    # Tính số giờ
    tong_so_gio_lam_viec_thuc_te = tuan_1 + tuan_2 + tuan_3 + tuan_4
    print(f"Tổng số giờ làm việc trong 4 tuần: {tong_so_gio_lam_viec_thuc_te}")
    if tong_so_gio_lam_viec_thuc_te > 160:
        tong_so_gio_lam_them = tong_so_gio_lam_viec_thuc_te - 160
        print(f"Tổng số giờ làm thêm trong 4 tuần: {tong_so_gio_lam_them}")
    elif tong_so_gio_lam_viec_thuc_te < 160:
        tong_so_gio_nghi = 160 - tong_so_gio_lam_viec_thuc_te
        prinf(f"Tổng số giờ nghỉ: {tong_so_gio_nghi}")
else:
    print("Không nhập giờ âm")
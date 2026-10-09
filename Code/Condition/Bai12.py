"""
    Câu 2: Tính tiền thưởng cho nhân viên
Một công ty cần tính tổng tiền lương thực nhận của một nhân viên dựa trên số ngày làm việc và kết quả đánh giá hiệu suất trong tháng.
Thực hiện yêu cầu:
1. Cho người dùng nhập các thông tin sau:
- Số ngày làm việc thực tế trong tháng (D, từ 0 đến 26 ngày).
- Tiền lương cơ bản mỗi ngày (dạng số thực float, phải lớn hơn 0).
- Điểm đánh giá hiệu suất làm việc (S, từ 0 đến 100).
2. Tính tiền lương theo số ngày làm việc thực tế:
- Tiền lương = Số ngày làm việc × Tiền lương mỗi ngày.
3. Dựa trên điểm đánh giá hiệu suất, tính tiền thưởng theo quy định:
- Nếu S ≥ 90: Thưởng 20% tiền lương.
- Nếu 75 ≤ S < 90: Thưởng 10% tiền lương.
- Nếu 60 ≤ S < 75: Thưởng 5% tiền lương.
- Nếu S < 60: Không được thưởng.
4. Kiểm tra số ngày làm việc để tính tiền phạt:
- Nếu D ≥ 24: Không bị phạt.
- Nếu 20 ≤ D < 24: Phạt 200.000 đồng.
- Nếu D < 20: Phạt 500.000 đồng.
5. Tính tổng tiền lương thực nhận theo công thức:
   Lương thực nhận = Tiền lương + Tiền thưởng − Tiền phạt.
6. In ra màn hình:
   - Tiền lương theo số ngày làm việc.
   - Tiền thưởng hiệu suất.
   - Tiền phạt.
   - Tổng tiền lương thực nhận.
"""
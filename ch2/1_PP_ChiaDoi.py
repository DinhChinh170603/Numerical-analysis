import math

# Định nghĩa hàm f(x)
def func(x):
    return x**2 - 3  # f(x) = x^2 - 3, ví dụ hàm số để tìm nghiệm

# Khởi tạo các giá trị đầu cuối
a = 1.7
b = 1.8

# Khởi tạo các tham số khác
TOL = 1e-5  # Sai số chấp nhận được
max_iteration = 1e6  # Số lần lặp tối đa

def bisection_method(a, b, TOL, max_iteration):
    i = 1  # Khởi tạo bộ đếm vòng lặp
    FA = func(a)  # Tính giá trị hàm tại điểm a

    while i <= max_iteration:  # Tiếp tục lặp nếu chưa đạt số lần lặp tối đa
        print(f'vòng lặp thứ {i}: ')
        p = a + (b - a) / 2  # Tính điểm giữa của khoảng [a, b]
        FP = func(p)  # Tính giá trị hàm tại điểm giữa p
        print(f'p = {p}, f(p) = {FP}')

        if FP == 0 or (b - a) / 2 < TOL:  # Kiểm tra điều kiện dừng
            # Kiểm tra điều kiện dừng của thuật toán, nếu giá trị hàm tại p bằng 0 hoặc độ rộng của khoảng [a, b] nhỏ hơn sai số cho phép.
            print(f'kết quả: p = {p}, f(p) = {FP}')
            return p  # Trả về nghiệm nếu tìm thấy

        if FA * FP > 0:  # Cập nhật lại khoảng [a, b] dựa trên dấu của giá trị hàm
            # Kiểm tra xem có cần thay đổi điểm a hay b để thu hẹp khoảng chứa nghiệm. Nếu f(a) và f(p) cùng dấu, cập nhật a = p, ngược lại thì b = p.
            a = p
            FA = FP
        else:
            b = p

        i = i + 1  # Tăng bộ đếm vòng lặp

    print(f'thất bại sau {i} vòng lặp')  # In thông báo thất bại nếu vượt quá số lần lặp

bisection_method(a, b, TOL, max_iteration)

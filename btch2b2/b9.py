import math

# Định nghĩa hàm f(x)
def func(x):
    return x**2 - 3

# Khởi tạo các giá trị đầu cuối
a = 1 # vì sqrt(3) nằm trong khoảng này
b = 2

# Khởi tạo các tham số khác
TOL = 1e-4  # Sai số chấp nhận được
max_iteration = 100  # Số lần lặp tối đa

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

# import math

# # Định nghĩa hàm g(x) theo bài toán
# def g(x):
#     return x**2 - 3

# # Phương pháp điểm bất động
# def fixpoint_method(p0, TOL, max_iteration):
#     """
#     Phương pháp điểm bất động để tìm nghiệm của phương trình f(x) = 0 bằng cách sử dụng g(x)
#     :param p0: Giá trị ban đầu
#     :param TOL: Ngưỡng sai số cho phép
#     :param max_iteration: Số lần lặp tối đa
#     :return: Nghiệm tìm được
#     """
#     i = 1  # Khởi tạo bộ đếm vòng lặp

#     while i <= max_iteration:
#         p = g(p0)  # Tính giá trị mới từ hàm g(x)
#         print(f'Vòng lặp thứ {i}:')
#         print(f'p0 = {p0:.10f} -> p = {p:.10f}')  # Chỉ in 10 chữ số sau dấu phẩy

#         # Kiểm tra điều kiện dừng của thuật toán
#         if abs(p - p0) < TOL:
#             print(f'Kết quả: p = {p:.10f}')
#             return p  # Trả về nghiệm nếu tìm thấy

#         p0 = p  # Cập nhật giá trị p0 cho lần lặp tiếp theo
#         i += 1  # Tăng bộ đếm vòng lặp

#     print('Thất bại sau', max_iteration, 'vòng lặp')
#     return None

# # Khởi tạo các tham số
# p0 = 1.5  # Giá trị ban đầu (bắt đầu gần giá trị thực của sqrt(3))
# TOL = 1e-4  # Ngưỡng sai số chấp nhận được
# max_iteration = 100  # Số lần lặp tối đa

# # Gọi hàm fixpoint_method để thực hiện phương pháp điểm bất động
# fixpoint_method(p0, TOL, max_iteration)
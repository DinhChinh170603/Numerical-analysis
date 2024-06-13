import math

# câu a
# Định nghĩa hàm f(x)
def f(x):
    return math.tan(math.pi * x) - 6

# # Khởi tạo các giá trị đầu cuối
# a = 0
# b = 0.48

# # Khởi tạo các tham số khác
# TOL = 1e-6  # Sai số chấp nhận được
# max_iteration = 10  # Số lần lặp tối đa

# def bisection_method(a, b, TOL, max_iteration):
#     i = 1  # Khởi tạo bộ đếm vòng lặp
#     FA = func(a)  # Tính giá trị hàm tại điểm a

#     while i <= max_iteration:  # Tiếp tục lặp nếu chưa đạt số lần lặp tối đa
#         print(f'vòng lặp thứ {i}: ')
#         p = a + (b - a) / 2  # Tính điểm giữa của khoảng [a, b]
#         FP = func(p)  # Tính giá trị hàm tại điểm giữa p
#         print(f'p = {p}, f(p) = {FP}')

#         if FP == 0 or (b - a) / 2 < TOL:  # Kiểm tra điều kiện dừng
#             # Kiểm tra điều kiện dừng của thuật toán, nếu giá trị hàm tại p bằng 0 hoặc độ rộng của khoảng [a, b] nhỏ hơn sai số cho phép.
#             print(f'kết quả: p = {p}, f(p) = {FP}')
#             return p  # Trả về nghiệm nếu tìm thấy

#         if FA * FP > 0:  # Cập nhật lại khoảng [a, b] dựa trên dấu của giá trị hàm
#             # Kiểm tra xem có cần thay đổi điểm a hay b để thu hẹp khoảng chứa nghiệm. Nếu f(a) và f(p) cùng dấu, cập nhật a = p, ngược lại thì b = p.
#             a = p
#             FA = FP
#         else:
#             b = p

#         i = i + 1  # Tăng bộ đếm vòng lặp

#     print(f'thất bại sau {i} vòng lặp')  # In thông báo thất bại nếu vượt quá số lần lặp

# bisection_method(a, b, TOL, max_iteration)


# câu b
# def func(x):
#     return math.tan(math.pi * x) - 6

# p0 = 0  # Giá trị ước lượng ban đầu p0
# p1 = 0.48  # Giá trị ước lượng ban đầu p1
# TOL = 1e-6  # Sai số chấp nhận được
# max_iteration = 10  # Số lần lặp tối đa

# def false_position_method(p0, p1, TOL, max_iteration):
#     i = 2  # Bắt đầu từ lần lặp thứ hai, theo thuật toán
#     q0 = func(p0)  # Tính f(p0)
#     q1 = func(p1)  # Tính f(p1)

#     while i <= max_iteration:  # Tiếp tục lặp nếu chưa đạt số lần lặp tối đa
#         p = p1 - q1 * (p1 - p0) / (q1 - q0)  # Tính giá trị mới p theo công thức False Position
#         #sử dụng giá trị hàm tại p0 và p1 để ước lượng nghiệm.
#         if abs(p - p1) < TOL:  # Kiểm tra điều kiện dừng của thuật toán
#             # Kiểm tra xem giá trị mới p có đủ gần với ước lượng trước đó p1 không. Nếu khoảng cách nhỏ hơn hoặc bằng sai số cho phép, thuật toán dừng lại và trả về nghiệm.
#             print(f'kết quả: p = {p}')
#             return p  # Trả về nghiệm nếu tìm thấy

#         q = func(p)  # Tính f(p) mới

#         if q * q1 < 0:  # Cập nhật giá trị p0, q0 nếu f(p) và f(p1) trái dấu
#             # nếu không, chỉ cập nhật p1 và q1.
#             p0 = p1
#             q0 = q1

#         p1 = p  # Cập nhật p1 và q1 cho lần lặp tiếp theo
#         q1 = q

#         i += 1  # Tăng bộ đếm vòng lặp

#     print(f'thất bại sau {i} vòng lặp')  # In thông báo thất bại nếu vượt quá số lần lặp

# false_position_method(p0, p1, TOL, max_iteration)

# câu c
# def func(x):
#     return math.tan(math.pi * x) - 6

# # Tham số khởi tạo
# p0 = 0  # Giá trị ước lượng ban đầu p0
# p1 = 0.48  # Giá trị ước lượng ban đầu p1
# TOL = 1e-6  # Sai số chấp nhận được
# max_iteration = 200  # Số lần lặp tối đa

# def secant_method(p0, p1, TOL, max_iteration):
#     i = 2  # Bắt đầu từ lần lặp thứ hai, theo thuật toán
#     q0 = func(p0)  # Tính f(p0)
#     q1 = func(p1)  # Tính f(p1)

#     while i <= max_iteration:  # Tiếp tục lặp nếu chưa đạt số lần lặp tối đa
#         p = p1 - q1 * (p1 - p0) / (q1 - q0)  # Tính giá trị mới p theo công thức Secant
#         # với q0 và q1 là các giá trị của hàm tại p0 và p1. Đây là phương pháp gần đúng để tìm nghiệm của phương trình phi tuyến không cần đạo hàm.
#         if abs(p - p1) < TOL:  # Kiểm tra điều kiện dừng của thuật toán
#             print(f'kết quả: p = {p}')
#             return p  # Trả về nghiệm nếu tìm thấy

#         # Cập nhật giá trị cho lần lặp tiếp theo
#         p0 = p1
#         q0 = q1
#         p1 = p
#         q1 = func(p)

#         i += 1  # Tăng bộ đếm vòng lặp

#     print(f'thất bại sau {i} vòng lặp')  # In thông báo thất bại nếu vượt quá số lần lặp

# secant_method(p0, p1, TOL, max_iteration)

# Sử dụng code khác

# def false_position(f, a, b, tol=1e-6, max_iter=10):
#     if f(a) * f(b) >= 0:
#         print("The function must have different signs at a and b.")
#         return None
#     for i in range(max_iter):
#         c = (a * f(b) - b * f(a)) / (f(b) - f(a))
#         if abs(f(c)) < tol:
#             return c
#         elif f(a) * f(c) < 0:
#             b = c
#         else:
#             a = c
#     return c

# # Áp dụng phương pháp False Position
# root_false_position = false_position(f, 0, 0.48)
# print(f'Nghiệm xấp xỉ bằng phương pháp False Position: {root_false_position}')

def secant_method(f, x0, x1, tol=1e-6, max_iter=10):
    for i in range(max_iter):
        if abs(f(x1) - f(x0)) < tol:
            return x1
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    return x1

# Áp dụng phương pháp Secant
root_secant = secant_method(f, 0, 0.48)
print(f'Nghiệm xấp xỉ bằng phương pháp Secant: {root_secant}')

import numpy as np
from scipy.interpolate import CubicSpline

# Bài 9 yêu cầu lặp lại Bài tập 5 bằng cách sử dụng các đường spline khép kín (clamped cubic splines) 
# đã được xây dựng trong Bài tập 7

# Dữ liệu điểm từ bài tập 7
data_a = np.array([[8.3, 17.56492], [8.6, 18.50515]])
data_b = np.array([[0.8, 0.22363362], [1.0, 0.65809197]])
data_c = np.array([[-0.5, -0.02475000], [-0.25, 0.33493750], [0.0, 1.10100000]])
data_d = np.array([[0.1, -0.62049958], [0.2, -0.28398668], [0.3, 0.00660095], [0.4, 0.24842440]])

# Dữ liệu từ bài tập 5
exercise_5_data = {
    'a': (8.4, 8.4),
    'b': (0.9, 0.9),
    'c': (-1/3, -1/3),
    'd': (0.25, 0.25)
}

# Hàm xây dựng spline bậc ba khép kín sử dụng scipy.interpolate.CubicSpline
def clamped_cubic_spline(data, bc_type):
    x = data[:, 0]  # Tọa độ x của các điểm
    y = data[:, 1]  # Tọa độ y của các điểm
    return CubicSpline(x, y, bc_type=bc_type)  # Trả về spline khép kín

# Hàm sử dụng spline khép kín để xấp xỉ f(x) và f'(x)
def approximate_values(spline, x):
    f_x = spline(x)  # Tính giá trị f(x) tại x
    f_x_deriv = spline(x, 1)  # Tính giá trị f'(x) tại x
    return f_x, f_x_deriv  # Trả về giá trị f(x) và f'(x)

# Hàm chính để giải bài tập
if __name__ == "__main__":
    # Định nghĩa điều kiện biên cho spline khép kín
    bc_a = ((1, 3.116256), (1, 3.151762))
    bc_b = ((1, 2.1691753), (1, 2.0466965))
    bc_c = ((1, 0.7510000), (1, 4.0020000))
    bc_d = ((1, 3.58502082), (1, 2.16529366))
    
    # Tạo các spline khép kín cho từng phần của bài tập
    splines = {
        'a': clamped_cubic_spline(data_a, bc_type=bc_a),
        'b': clamped_cubic_spline(data_b, bc_type=bc_b),
        'c': clamped_cubic_spline(data_c, bc_type=bc_c),
        'd': clamped_cubic_spline(data_d, bc_type=bc_d)
    }
    
    # Tính và in kết quả xấp xỉ cho từng phần của bài tập
    for key, (x_val, x_prime_val) in exercise_5_data.items():
        spline = splines[key]  # Lấy spline tương ứng
        f_x, f_x_prime = approximate_values(spline, x_val)  # Tính f(x) và f'(x) tại x_val
        f_prime_x, f_prime_x_prime = approximate_values(spline, x_prime_val)  # Tính f(x) và f'(x) tại x_prime_val
        print(f"Approximation for part {key}:")
        print(f"f({x_val}) = {f_x}, f'({x_prime_val}) = {f_x_prime}")
        print(f"Actual Error for f({x_val}): {f_x - f_x_prime}, f'({x_prime_val}): {f_prime_x - f_prime_x_prime}\n")

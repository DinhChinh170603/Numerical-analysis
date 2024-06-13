import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import quad

# Hàm tính giá trị thực của tích phân
def real_integral_exp_neg_x():
    return quad(lambda x: np.exp(-x), 0, 1)[0]

# Hàm xây dựng spline khép kín
def clamped_cubic_spline(x, y, bc_type):
    return CubicSpline(x, y, bc_type=bc_type)

# Dữ liệu điểm từ bài tập 16
x_values = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
y_values = np.exp(-x_values)

# Điều kiện biên cho spline khép kín với f'(0) = -1, f'(1) = -e^-1
bc_type = ((1, -1.0), (1, -np.exp(-1)))

# Xây dựng spline
spline = clamped_cubic_spline(x_values, y_values, bc_type)

# Tính tích phân của spline trên đoạn [0, 1]
integral_spline, _ = quad(spline, 0, 1)
real_integral = real_integral_exp_neg_x()

# Tính đạo hàm bậc nhất và bậc hai tại x = 0.5
f_prime_0_5 = spline(0.5, 1)
f_double_prime_0_5 = spline(0.5, 2)

# Giá trị thực tế của f'(0.5) và f''(0.5) cho f(x) = e^-x
real_f_prime_0_5 = -np.exp(-0.5)
real_f_double_prime_0_5 = np.exp(-0.5)

print(f"Tích phân của spline trên đoạn [0, 1]: {integral_spline}")
print(f"Tích phân thực: {real_integral}")
print(f"Đạo hàm bậc nhất tại x=0.5 của spline: {f_prime_0_5}")
print(f"Đạo hàm bậc nhất thực tại x=0.5: {real_f_prime_0_5}")
print(f"Đạo hàm bậc hai tại x=0.5 của spline: {f_double_prime_0_5}")
print(f"Đạo hàm bậc hai thực tại x=0.5: {real_f_double_prime_0_5}")

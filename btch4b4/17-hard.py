import numpy as np
from scipy.interpolate import CubicSpline
import scipy.integrate as spi

# Bài 17 yêu cầu lặp lại Bài tập 15, nhưng thay vì sử dụng spline tự nhiên
# thì cần sử dụng spline khép kín với điều kiện biên 𝑓′(0)=𝑓′(1)=0

# Dữ liệu điểm từ bài tập 15
x_vals = np.array([0, 0.25, 0.5, 0.75, 1.0])  # Tọa độ x
f_vals_15 = np.cos(np.pi * x_vals)  # Giá trị f(x) = cos(pi * x) tại các điểm x

# Xây dựng spline khép kín (clamped cubic spline) cho bài tập 17 với điều kiện biên f'(0) = f'(1) = 0
spline_17 = CubicSpline(x_vals, f_vals_15, bc_type=((1, 0.0), (1, 0.0)))

# Tính tích phân của spline khép kín trên đoạn [0, 1]
integral_17, _ = spi.quad(spline_17, 0, 1)

# Tính giá trị thực của tích phân ∫0^1 cos(pi * x) dx = (1 / pi) * sin(pi * x) từ 0 đến 1
true_integral_17 = (1 / np.pi) * (np.sin(np.pi * 1) - np.sin(np.pi * 0))

# Tính đạo hàm cấp 1 và cấp 2 của spline khép kín tại x = 0.5
f_prime_17 = spline_17(0.5, 1)
f_double_prime_17 = spline_17(0.5, 2)

# Giá trị thực của f'(0.5) và f''(0.5)
true_f_prime_17 = -np.pi * np.sin(np.pi * 0.5)
true_f_double_prime_17 = -np.pi**2 * np.cos(np.pi * 0.5)

# In kết quả
print("Bài tập 17 - Sử dụng spline khép kín")
print(f"Tích phân của spline khép kín trên đoạn [0, 1]: {integral_17}")
print(f"Giá trị thực của tích phân: {true_integral_17}")
print(f"Sai số tích phân: {abs(integral_17 - true_integral_17)}")
print(f"f'(0.5) của spline khép kín: {f_prime_17}")
print(f"f'(0.5) thực: {true_f_prime_17}")
print(f"Sai số f'(0.5): {abs(f_prime_17 - true_f_prime_17)}")
print(f"f''(0.5) của spline khép kín: {f_double_prime_17}")
print(f"f''(0.5) thực: {true_f_double_prime_17}")
print(f"Sai số f''(0.5): {abs(f_double_prime_17 - true_f_double_prime_17)}")

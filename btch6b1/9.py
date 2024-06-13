from math import tan, exp

class DerivativeApproximation:
    def midpoint_rule_3point(self, f, x0, h):
        d = (f(x0 + h) - f(x0 - h)) / (2.0 * h)
        return round(d, 4)

    def endpoint_rule_3point(self, f, x0, h):
        d = (-3 * f(x0) + 4 * f(x0 + h) - f(x0 + 2 * h)) / (2.0 * h)
        return round(d, 4)

    def midpoint_rule_5point(self, f, x0, h):
        d = (f(x0 - 2 * h) - 8 * f(x0 - h) + 8 * f(x0 + h) - f(x0 + 2 * h)) / (12.0 * h)
        return round(d, 4)

    def endpoint_rule_5point(self, f, x0, h):
        d = (-25 * f(x0) + 48 * f(x0 + h) - 36 * f(x0 + 2 * h) + 16 * f(x0 + 3 * h) - 3 * f(x0 + 4 * h)) / (12.0 * h)
        return round(d, 4)

# Định nghĩa các hàm f tại các điểm cụ thể trong bảng
def f_a(x):
    return tan(x)

def f_b(x):
    return exp(x / 3) + x**2

# Các điểm cần tính và bước nhảy h
x_values_a = [2.1, 2.2, 2.3, 2.4, 2.5, 2.6]
x_values_b = [-3.0, -2.8, -2.6, -2.4, -2.2, -2.0]
h = 0.1

# Tạo đối tượng DerivativeApproximation
dx = DerivativeApproximation()

# Tính toán và in kết quả cho bảng a
print("Bảng a:")
for x in x_values_a:
    if x == x_values_a[0] or x == x_values_a[-1]:  # Dùng endpoint formula cho điểm đầu và cuối
        f_prime_3point = dx.endpoint_rule_3point(f_a, x, h)
        f_prime_5point = dx.endpoint_rule_5point(f_a, x, h)
    else:  # Dùng midpoint formula cho các điểm còn lại
        f_prime_3point = dx.midpoint_rule_3point(f_a, x, h)
        f_prime_5point = dx.midpoint_rule_5point(f_a, x, h)
    print(f"x = {x}, f'(x) ≈ {f_prime_3point} (3-point), {f_prime_5point} (5-point)")

# Tính toán và in kết quả cho bảng b
print("\nBảng b:")
for x in x_values_b:
    if x == x_values_b[0] or x == x_values_b[-1]:  # Dùng endpoint formula cho điểm đầu và cuối
        f_prime_3point = dx.endpoint_rule_3point(f_b, x, h)
        f_prime_5point = dx.endpoint_rule_5point(f_b, x, h)
    else:  # Dùng midpoint formula cho các điểm còn lại
        f_prime_3point = dx.midpoint_rule_3point(f_b, x, h)
        f_prime_5point = dx.midpoint_rule_5point(f_b, x, h)
    print(f"x = {x}, f'(x) ≈ {f_prime_3point} (3-point), {f_prime_5point} (5-point)")

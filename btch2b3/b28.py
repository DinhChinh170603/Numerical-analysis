import math
from scipy.optimize import fsolve

def concentration(t, A):
    return A * t * math.exp(-t / 3)

def find_A_for_max_concentration(max_concentration, t):
    return max_concentration / (t * math.exp(-t / 3))

def dcdt(t, A):
    return A * (1 - t / 3) * math.exp(-t / 3)

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("The function must have different signs at a and b.")
        return None
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

# Tìm thời điểm t tối đa bằng phương pháp Bisection
A = 1  # Chọn giá trị A ban đầu
t_max_bisection = bisection_method(lambda t: dcdt(t, A), 0.1, 10)
A = find_A_for_max_concentration(1, t_max_bisection)

print(f'Giá trị của A để đạt nồng độ tối đa an toàn (Bisection): {A}')
print(f'Thời điểm t khi nồng độ đạt tối đa (Bisection): {t_max_bisection}')

def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# Hàm đạo hàm của phương trình nồng độ
def concentration_prime(t, A):
    return A * (1 - t / 3) * math.exp(-t / 3)

# Tìm thời điểm t khi nồng độ là 0.25 mg/mL bằng phương pháp Newton
t_025_newton = newton_method(lambda t: concentration(t, A) - 0.25, lambda t: concentration_prime(t, A), 1)
print(f'Thời điểm tiêm liều bổ sung khi nồng độ giảm xuống 0.25 mg/mL (Newton): {t_025_newton} giờ')

def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        if abs(f(x1) - f(x0)) < tol:
            return x1
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    return x1

# Giả sử 75% của A được tiêm lần hai
A2 = 0.75 * A

# Hàm để tính tổng nồng độ từ hai liều tiêm
def total_concentration(t, t1, A1, A2):
    return concentration(t, A1) + concentration(t - t1, A2)

# Tìm thời điểm t cho liều thứ ba bằng phương pháp Secant
t_third_secant = secant_method(lambda t: total_concentration(t, t_025_newton, A, A2) - 0.25, t_025_newton, t_025_newton + 1)
print(f'Thời điểm tiêm liều thuốc thứ ba (Secant): {t_third_secant} giờ')

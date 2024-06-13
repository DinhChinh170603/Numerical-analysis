import math

def f(x):
    return x ** 3 - 2* (x ** 2) - 5

def secant_method_simple(f, p0, p1, tol=1e-6, max_iter=10):
    for _ in range(max_iter):
        if abs(f(p1) - f(p0)) < tol:
            return p1
        p2 = (f(p1) * p0 - f(p0) * p1) / (f(p1) - f(p0))
        if abs(p2 - p1) < tol:
            return p2
        p0, p1 = p1, p2
    return p1

def secant_method(f, p0, p1, tol=1e-6, max_iter=10):
    for _ in range(max_iter):
        if abs(f(p1) - f(p0)) < tol:
            return p1
        p2 = p1 - f(p1) * (p1 - p0) / (f(p1) - f(p0))
        if abs(p2 - p1) < tol:
            return p2
        p0, p1 = p1, p2
    return p1

# Áp dụng cả hai phương pháp
root_secant_simple = secant_method_simple(f, 1, 4)
root_secant = secant_method(f, 1, 4)

# In kết quả
print(f'Nghiệm xấp xỉ bằng phương pháp Secant (đơn giản): {root_secant_simple}')
print(f'Nghiệm xấp xỉ bằng phương pháp Secant (Algorithm 2.4): {root_secant}')

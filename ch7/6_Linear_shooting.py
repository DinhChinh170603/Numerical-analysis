import numpy as np
import math

# Các hàm này biểu diễn các hệ số trong phương trình vi phân.
p = lambda x: x
q = lambda x: x * 2
r = lambda x: x + 3

# Hàm tính u (phương trình thứ nhất)
def func1(x, y: np.ndarray):
    # Hàm này tính giá trị của u tại điểm x với giá trị y hiện tại.
    res = np.ndarray(1)
    res[0] = p(x) * y[0] + q(x) * y[1] + r(x)
    return res

# Hàm tính v (phương trình thứ hai)
def func2(x, y: np.ndarray):
    # Hàm này tính giá trị của v tại điểm x với giá trị y hiện tại.
    res = np.ndarray(1)
    res[0] = p(x) * y[0] + q(x) * y[1]
    return res

# Hàm Runge-Kutta bậc 4
def RK4(df, x, y: np.array, h):
    k1 = df(x, y)
    k2 = df(x + 0.5 * h, y + 0.5 * h * k1)
    k3 = df(x + 0.5 * h, y + 0.5 * h * k2)
    k4 = df(x + h, y + h * k3)
    y1 = y + h/6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return y1

# Hàm Linear Shooting
def linear_shooting(a, b, alpha, beta, N, TOL):
    # Bước 1: Tính bước nhảy h
    h = (b - a) / N

    # Khởi tạo u và v
    u = np.array([alpha, 0])
    v = np.array([0, 1])

    # Bước 2: Vòng lặp từ 0 đến N-1
    for i in range(N):
        x = a + i * h

        # Bước 3 + 4: Sử dụng phương pháp Runge-Kutta bậc 4
        u = RK4(func1, x, u, h)
        v = RK4(func2, x, v, h)

    # Bước 5: Tính w1 và w2 ban đầu
    w1 = alpha
    w2 = (beta - u[0]) / v[0]

    # In kết quả ban đầu
    print(f'Giá trị khởi tạo:\na = {a}\nw1 = {w1}\nw2 = {w2}')

    # Bước 6: Vòng lặp từ 1 đến N
    x = a
    for i in range(1, N + 1):
        W1 = u[0] + w2 * v[0]
        W2 = u[1] + w2 * v[1]
        x = a + i * h
        print(f'x = {x}, W1 = {W1}, W2 = {W2}')

    return W1, W2

# Ví dụ sử dụng phương pháp Linear Shooting
a = 0
b = 1
alpha = 1
beta = 2
N = 10
TOL = 1e-6

linear_shooting(a, b, alpha, beta, N, TOL)

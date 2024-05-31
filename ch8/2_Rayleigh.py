import numpy as np

def piecewise_linear_rayleigh_ritz(n, x, p, q, f):
    h = np.diff(x)  # Bước nhảy giữa các điểm
    phi = np.zeros((n + 1, n + 1))  # Ma trận phi

    # Step 2: Định nghĩa cơ sở phi
    for i in range(1, n):
        phi[i, i-1] = (x[i+1] - x[i]) / h[i-1]
        phi[i, i] = (x[i] - x[i-1]) / h[i]
        phi[i, i+1] = (x[i+1] - x[i]) / h[i]

    # Step 3: Tính toán các hệ số Q
    Q = np.zeros((n + 1, n + 1))
    for i in range(1, n):
        Q[i, i-1] = p(x[i]) / h[i-1]
        Q[i, i] = q(x[i])
        Q[i, i+1] = p(x[i]) / h[i]

    # Step 4: Tính toán các hệ số a và b
    a = np.zeros(n + 1)
    b = np.zeros(n + 1)
    for i in range(1, n):
        a[i] = Q[i, i-1] + Q[i, i] + Q[i, i+1]
        b[i] = f(x[i])

    # Step 5: Thiết lập giá trị biên
    a[0] = Q[0, 0] + Q[0, 1]
    b[0] = f(x[0])
    a[-1] = Q[-1, -2] + Q[-1, -1]
    b[-1] = f(x[-1])

    # Step 6: Giải hệ phương trình tuyến tính
    c = np.zeros(n + 1)
    for i in range(1, n):
        c[i] = a[i] / b[i]

    return c

# Ví dụ áp dụng
n = 20
x = np.linspace(0, 1, n + 1)
p = lambda x: x
q = lambda x: x * 2
f = lambda x: x + 3

c = piecewise_linear_rayleigh_ritz(n, x, p, q, f)

print("Hệ số c:")
print(c)

# Câu a: cminh rằng dãy xn xác định bởi xn = ... hội tụ đến căn 2 khi x0 > căn 2
def sequence_xn(x0, n):
    x = x0
    for _ in range(n):
        x = 0.5 * x + 1 / x
    return x

# Chọn giá trị ban đầu x0 > sqrt(2)
x0 = 2.0
n = 100  # Số lần lặp

# Tính giá trị của x_n sau 100 lần lặp
xn = sequence_xn(x0, n)
print(f'Giá trị của x_n sau {n} lần lặp là: {xn}')

# Câu b: cminh nếu 0 < x0 < căn 2, thì x1 > căn 2
import math

def check_x1_greater_sqrt2(x0):
    x1 = 0.5 * x0 + 1 / x0
    return x1 > math.sqrt(2)

# Kiểm tra với giá trị x0 trong khoảng (0, sqrt(2))
x0 = 1.0
result = check_x1_greater_sqrt2(x0)
print(f'Với x0 = {x0}, x1 > sqrt(2) là: {result}')

# Câu c: cminh dãy trong câu a hội tụ đến căn 2 bất kỳ khi nào x0 > 0
def sequence_converge_sqrt2(x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = 0.5 * x + 1 / x
        if abs(x_new - x) < tol:
            return x_new, i
        x = x_new
    return x, max_iter

# Chọn giá trị ban đầu x0 > 0
x0 = 0.1

# Kiểm tra hội tụ
sqrt2 = math.sqrt(2)
xn, iterations = sequence_converge_sqrt2(x0)
print(f'Giá trị của x_n sau {iterations} lần lặp là: {xn}, hội tụ đến sqrt(2): {abs(xn - sqrt2) < 1e-6}')

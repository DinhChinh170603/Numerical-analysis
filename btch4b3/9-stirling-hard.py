import numpy as np

def forward_difference_table(x, y):
    n = len(y)
    fd_table = np.zeros((n, n)) # Tạo bảng sai phân trước.
    fd_table[:, 0] = y # Điền cột đầu tiên của bảng với giá trị y tại các điểm.
    for j in range(1, n):
        for i in range(n - j):
            fd_table[i, j] = fd_table[i + 1, j - 1] - fd_table[i, j - 1] # Tính các giá trị sai phân trước.
    return fd_table

def newton_forward_difference(x, y, value):
    n = len(x)
    fd_table = forward_difference_table(x, y)
    h = x[1] - x[0] # Tính khoảng cách giữa các điểm x.
    p = (value - x[0]) / h # Tính giá trị p cho công thức Newton forward-difference.
    result = y[0]
    factorial = 1
    for i in range(1, n):
        factorial *= i
        # Tính giá trị nội suy bằng công thức Newton forward-difference.
        result += (fd_table[0, i] / factorial) * np.prod([p - k for k in range(i)])
    return result

# Dữ liệu cho bài 9a
x = np.array([0.0, 0.2, 0.4, 0.6, 0.8])
y = np.array([1.00000, 1.22140, 1.49182, 1.82212, 2.22554])

# Giá trị cần nội suy tại x = 0.05
value = 0.05
approx_y = newton_forward_difference(x, y, value)
print("Câu 9a:")
print(f"Giá trị nội suy tại x = {value} là y = {approx_y}")

def backward_difference_table(x, y): 
    n = len(y)
    bd_table = np.zeros((n, n)) # Tạo bảng sai phân sau.
    bd_table[:, 0] = y
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            bd_table[i, j] = bd_table[i, j - 1] - bd_table[i - 1, j - 1]
    return bd_table

def newton_backward_difference(x, y, value):
    n = len(x)
    bd_table = backward_difference_table(x, y)
    h = x[1] - x[0]
    p = (value - x[-1]) / h
    result = y[-1]
    factorial = 1
    for i in range(1, n):
        factorial *= i
        # Tính giá trị nội suy bằng công thức Newton backward-difference.
        result += (bd_table[-1, i] / factorial) * np.prod([p + k for k in range(i)])
    return result

# Giá trị cần nội suy tại x = 0.65
value = 0.65
approx_y = newton_backward_difference(x, y, value)
print("\nCâu 9b:")
print(f"Giá trị nội suy tại x = {value} là y = {approx_y}")

def stirling_interpolation(x, y, value):
    n = len(x)
    h = x[1] - x[0]
    s = (value - x[n // 2]) / h # Tính giá trị s cho công thức Stirling.
    fd_table = forward_difference_table(x, y)

    result = y[n // 2]
    sum_term = 0
    factorial = 1
    for i in range(1, (n + 1) // 2):
        term = (fd_table[n // 2 - i, 2 * i - 1] + fd_table[n // 2 - i, 2 * i]) / 2
        sum_term += term * (s * np.prod([(s ** 2 - k ** 2) for k in range(1, i)])) / factorial
        factorial *= (2 * i) * (2 * i + 1)
        result += sum_term # Tính giá trị nội suy bằng công thức Stirling.
    return result

# Giá trị cần nội suy tại x = 0.43
value = 0.43
approx_y = stirling_interpolation(x, y, value)
print("\nCâu 9c:")
print(f"Giá trị nội suy tại x = {value} là y = {approx_y}")


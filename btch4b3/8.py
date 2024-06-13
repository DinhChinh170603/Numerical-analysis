import numpy as np

def divided_differences(points: np.ndarray):
    """ Tính bảng sai phân chia cho Newton's polynomial interpolation. """
    n = len(points)
    f = np.zeros((n, n))  # Khởi tạo bảng sai phân
    
    # Điền cột đầu tiên với giá trị y tại các điểm
    for i in range(n):
        f[i][0] = points[i][1]
    
    # Tính các sai phân chia
    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i + 1][j - 1] - f[i][j - 1]) / (points[i + j][0] - points[i][0])
    
    return f[0]  # Trả về các hệ số sai phân chia cho đa thức nội suy

def newton_polynomial(points: np.ndarray, x: float):
    """ Tính giá trị nội suy tại x bằng đa thức Newton. """
    coefficients = divided_differences(points)  # Tính hệ số sai phân chia
    n = len(points)
    result = coefficients[0]  # Khởi tạo giá trị đầu tiên của đa thức là hệ số tự do
    product_term = 1  # Biến lưu tích các (x - x_i)
    for i in range(1, n):
        product_term *= (x - points[i - 1][0])  # Tính tích các (x - x_i)
        result += coefficients[i] * product_term  # Cập nhật giá trị của đa thức
    return result

# Dữ liệu điểm cho bài 8a
points_8a = np.array([
    [0.0, -6.00000],
    [0.1, -5.89483],
    [0.3, -5.65014],
    [0.6, -5.17788],
    [1.0, -4.28172]
], dtype=float)

# Xây dựng đa thức nội suy bậc 4 cho bài 8a
approx_points_8a = [0.0, 0.1, 0.3, 0.6, 1.0]
print("Bài 8a:")
for x in approx_points_8a:
    y = newton_polynomial(points_8a, x)  # Tính giá trị nội suy tại các điểm x
    print(f"Giá trị nội suy bậc 4 tại x = {x} là y = {y}")

# Dữ liệu điểm cho bài 8b bao gồm thêm điểm f(1.1) = -3.99583
points_8b = np.array([
    [0.0, -6.00000],
    [0.1, -5.89483],
    [0.3, -5.65014],
    [0.6, -5.17788],
    [1.0, -4.28172],
    [1.1, -3.99583]
], dtype=float)

# Xây dựng đa thức nội suy bậc 5 cho bài 8b
approx_points_8b = [0.0, 0.1, 0.3, 0.6, 1.0, 1.1]
print("\nBài 8b:")
for x in approx_points_8b:
    y = newton_polynomial(points_8b, x)  # Tính giá trị nội suy tại các điểm x
    print(f"Giá trị nội suy bậc 5 tại x = {x} là y = {y}")

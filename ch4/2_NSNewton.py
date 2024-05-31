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
    coefficients = divided_differences(points)
    n = len(points)
    result = coefficients[0]
    product_term = 1
    for i in range(1, n):
        product_term *= (x - points[i - 1][0])
        result += coefficients[i] * product_term
    return result

# Ví dụ sử dụng
points = np.array([[1, 2], [2, 4], [3, 6]])  # Mảng điểm [x, y]
approx_point = 7  # Điểm x cần nội suy
print("Giá trị nội suy tại x =", approx_point, "là y =", newton_polynomial(points, approx_point))

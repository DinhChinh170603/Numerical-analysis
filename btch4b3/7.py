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
            # Tính các giá trị sai phân chia dựa trên các cột trước đó và hiệu của các giá trị x tương ứng.
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

# Dữ liệu điểm
points = np.array([ #  point: Các điểm dữ liệu ban đầu.
    [-0.1, 5.3000],
    [0.0, 2.0000],
    [0.2, 3.1900],
    [0.3, 1.0000]
], dtype=float)

# Xây dựng đa thức nội suy bậc 3
approx_points = [-0.1, 0.0, 0.2, 0.3] # approx_points: Các điểm cần nội suy cho đa thức bậc 3.
print("Bài 7a:")
for x in approx_points:
    y = newton_polynomial(points, x)  # Tính giá trị nội suy tại các điểm x
    print(f"Giá trị nội suy bậc 3 tại x = {x} là y = {y}")

print("\n")
# Câu b

# Thêm điểm f(0.35) = 0.97260 và xây dựng đa thức bậc 4
points_with_new = np.array([ # points_with_new: Các điểm dữ liệu bao gồm điểm mới cho đa thức bậc 4.
    [-0.1, 5.3000],
    [0.0, 2.0000],
    [0.2, 3.1900],
    [0.3, 1.0000],
    [0.35, 0.97260]
], dtype=float)

approx_points_new = [-0.1, 0.0, 0.2, 0.3, 0.35] # approx_points_new: Các điểm cần nội suy cho đa thức bậc 4.
print("Bài 7b:")
for x in approx_points_new:
    y = newton_polynomial(points_with_new, x)  # Tính giá trị nội suy tại các điểm x
    print(f"Giá trị nội suy bậc 4 tại x = {x} là y = {y}")

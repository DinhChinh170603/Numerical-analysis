import numpy as np
import math

def lagrange_interpolation(points: np.ndarray, approx_point: float) -> float:
    """ Nội suy Lagrange tại điểm approx_point dựa trên các điểm cho trước.
    Args:
        points (np.ndarray): Mảng 2D của các điểm dữ liệu, mỗi điểm là một cặp [x, y].
        approx_point (float): Điểm mà tại đó giá trị y cần được nội suy.
    
    Returns:
        float: Giá trị y nội suy tại điểm approx_point.
    """
    n = len(points)  # Số lượng điểm
    result = 0  # Khởi tạo kết quả nội suy

    # Vòng lặp qua mỗi điểm để tính các phần tử của tổng trong công thức Lagrange
    for i in range(n):
        # Tính tử số bằng cách nhân các (x - x_j) với j khác i
        numerator = np.prod([approx_point - points[j, 0] for j in range(n) if j != i])
        # Tính mẫu số bằng cách nhân các (x_i - x_j) với j khác i
        denominator = np.prod([points[i, 0] - points[j, 0] for j in range(n) if j != i])

        # Cập nhật kết quả bằng cách cộng dồn các thành phần của đa thức nội suy
        result += points[i, 1] * numerator / denominator

    return result

# Dữ liệu từ bài tập 5
data = {
    "a": np.array([[8.1, 16.94410], [8.3, 17.56492], [8.6, 18.50515], [8.7, 18.82091]]),
    "b": np.array([[-1/3, -0.07181250], [-0.5, -0.02475000], [-0.25, 0.33493750], [0, 1.10100000]]),
    "c": np.array([[0.1, 0.62049958], [0.2, -0.28398668], [0.3, 0.00660095], [0.4, 0.24842440]]),
    "d": np.array([[0.6, -0.17694460], [0.7, 0.01375227], [0.8, 0.22363362], [0.9, 0.65809197]])
}

# Các điểm cần nội suy từ bài tập 5
approx_points = {
    "a": 8.4,
    "b": -1/3,
    "c": 0.25,
    "d": 0.9
}

# Nội suy và in kết quả
for key in data:
    points = data[key]
    approx_point = approx_points[key]
    interpolated_value = lagrange_interpolation(points, approx_point)
    print(f"Giá trị nội suy tại {approx_point} cho phần {key} là {interpolated_value}")


# Các hàm cần nội suy từ bài tập 7
functions = {
    "a": lambda x: x * math.log(x),
    "b": lambda x: x**3 + 4.001 * x**2 + 4.002 * x + 1.101,
    "c": lambda x: x * math.cos(x) - 2 * x**2 + 3 * x - 1,
    "d": lambda x: math.sin(math.exp(x) - 2)
}

# Tính toán và so sánh sai số cho từng phần
for key in data:
    points = data[key]
    approx_point = approx_points[key]
    interpolated_value = lagrange_interpolation(points, approx_point)
    actual_value = functions[key](approx_point)
    error = abs(actual_value - interpolated_value)
    print(f"Sai số thực tế tại {approx_point} cho phần {key} là {error}")


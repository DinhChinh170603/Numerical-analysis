import math
import numpy as np

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

# Dữ liệu từ bài tập 6
data = {
    "a": np.array([[0, 1], [0.25, 1.64872], [0.5, 2.71828], [0.75, 4.48169]]),
    "b": np.array([[0, 1.93750], [-0.5, 1.33203], [-0.25, 0.800781], [0.5, 0.687500]]),
    "c": np.array([[0.1, -0.29004986], [0.2, -0.56079734], [0.3, -0.81401972], [0.4, -1.0526302]]),
    "d": np.array([[-1, 0.86199840], [-0.5, 0.95802009], [0, 1.0986123], [0.5, 1.2943767]])
}

# Các điểm cần nội suy từ bài tập 6
approx_points = {
    "a": 0.43,
    "b": -1/3,
    "c": 0.18,
    "d": 0.25
}

# Nội suy và in kết quả
for key in data:
    points = data[key]
    approx_point = approx_points[key]
    interpolated_value = lagrange_interpolation(points, approx_point)
    print(f"Giá trị nội suy tại {approx_point} cho phần {key} là {interpolated_value}")


# Các hàm cần nội suy từ bài tập 8
functions = {
    "a": lambda x: math.exp(2 * x),
    "b": lambda x: x**4 - x**3 + x**2 - x + 1,
    "c": lambda x: x**2 * math.cos(x) - 3 * x,
    "d": lambda x: math.log(math.exp(x) + 2)
}

# Tính toán và so sánh sai số cho từng phần
for key in data:
    points = data[key]
    approx_point = approx_points[key]
    interpolated_value = lagrange_interpolation(points, approx_point)
    actual_value = functions[key](approx_point)
    error = abs(actual_value - interpolated_value)
    print(f"Sai số thực tế tại {approx_point} cho phần {key} là {error}")

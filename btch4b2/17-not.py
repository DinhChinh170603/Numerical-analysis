# Bài này không chạy được code

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
        xi, yi = points[i]
        # Tạo đa thức cơ sở L_i(x)
        li = np.poly1d([1.0])
        for j in range(n):
            if j != i:
                xj = points[j, 0]
                li *= np.poly1d([1.0, -xj]) / (xi - xj)
        
        # Cập nhật đa thức nội suy
        result += li * yi

    return result(approx_point)

def generate_log_table(step_size: float) -> np.ndarray:
    """ Tạo bảng logarit cơ số 10 từ x = 1 đến x = 10 với bước nhảy step_size.
    Args:
        step_size (float): Bước nhảy giữa các giá trị x.
    
    Returns:
        np.ndarray: Bảng logarit gồm các cặp [x, log10(x)].
    """
    x_values = np.arange(1, 10 + step_size, step_size)
    log_values = np.log10(x_values)
    return np.column_stack((x_values, log_values))

def check_accuracy(step_size: float, tolerance: float = 1e-6) -> bool:
    """ Kiểm tra độ chính xác của nội suy Lagrange với bảng logarit và bước nhảy step_size.
    Args:
        step_size (float): Bước nhảy giữa các giá trị x.
        tolerance (float): Ngưỡng sai số cho phép.
    
    Returns:
        bool: True nếu độ chính xác đạt yêu cầu, ngược lại là False.
    """
    log_table = generate_log_table(step_size)
    x_test = np.arange(1, 10 + step_size, step_size / 2)
    for x in x_test:
        if x not in log_table[:, 0]:
            interpolated_value = lagrange_interpolation(log_table, x)
            actual_value = np.log10(x)
            error = abs(interpolated_value - actual_value)
            if error > tolerance:
                return False
    return True

# Tìm bước nhảy lớn nhất thỏa mãn yêu cầu độ chính xác
def find_max_step_size(tolerance: float = 1e-6) -> float:
    step_size = 1.0
    while not check_accuracy(step_size, tolerance):
        step_size /= 2
    return step_size

# Tìm bước nhảy lớn nhất
max_step_size = find_max_step_size()
print(f"Bước nhảy lớn nhất thỏa mãn độ chính xác {10**-6} là: {max_step_size}")

# Kiểm tra xem x = 10 có nằm trong bảng không
log_table = generate_log_table(max_step_size)
if 10 in log_table[:, 0]:
    print("Giá trị x = 10 nằm trong bảng.")
else:
    print("Giá trị x = 10 không nằm trong bảng.")

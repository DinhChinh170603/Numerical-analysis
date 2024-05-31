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

# Ví dụ sử dụng
if __name__ == "__main__":
    points = np.array([[1, 2], [2, 4], [3, 6]])  # Điểm dữ liệu
    approx_point = 7  # Điểm cần nội suy
    print("Giá trị nội suy tại x =", approx_point, "là y =", lagrange_interpolation(points, approx_point))

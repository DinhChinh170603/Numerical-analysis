import numpy as np
import scipy.linalg as sla

def cubic_spline(points):
    """
    Tính các hệ số cho phép nội suy spline bậc ba từ một tập hợp các điểm dữ liệu.
    
    Args:
    points (np.ndarray): Mảng các điểm dữ liệu, mỗi điểm là một cặp [x, y].
    
    Returns:
    np.ndarray: Mảng chứa các hệ số [a, b, c, d] của đa thức bậc ba cho mỗi đoạn của spline.
    """
    n = len(points) - 1  # Số đoạn spline
    x = points[:, 0]  # Tọa độ x của các điểm
    y = points[:, 1]  # Tọa độ y của các điểm

    # Bước 1: Tính h và alpha
    h = np.diff(x)  # Khoảng cách giữa các điểm x liên tiếp
    alpha = np.diff(y) / h  # Tốc độ thay đổi y giữa các điểm

    # Bước 2: Thiết lập hệ phương trình để giải c
    A = np.zeros((n + 1, n + 1))  # Khởi tạo ma trận hệ số
    b = np.zeros(n + 1)  # Khởi tạo vector kết quả

    # Điều kiện biên spline tự nhiên
    A[0, 0] = 1
    A[-1, -1] = 1

    for i in range(1, n):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        b[i] = 3 * (alpha[i] - alpha[i - 1])

    # Bước 3: Giải hệ phương trình tuyến tính cho c
    c = sla.solve(A, b)

    # Bước 4: Tính b, d và gán a
    d = np.diff(c) / (3 * h)
    b = alpha - h * (2 * c[:-1] + c[1:]) / 3
    a = y[:-1]

    # Mỗi hàng trong coeffs tương ứng với [a, b, c, d] cho mỗi đoạn
    coeffs = np.vstack([a, b, c[:-1], d]).T

    return coeffs

# Ví dụ sử dụng
points = np.array([[0, 0], [1, 2], [2, 3], [3, 2]])
coefficients = cubic_spline(points)
print("Hệ số spline bậc ba cho mỗi đoạn:")
for i, coeff in enumerate(coefficients):
    print(f"Đoạn {i}: a={coeff[0]}, b={coeff[1]}, c={coeff[2]}, d={coeff[3]}")

import numpy as np
import scipy.linalg as sla

def cubic_spline(points, fpa, fpb):
    """
    Tính các hệ số cho phép nội suy spline bậc ba từ một tập hợp các điểm dữ liệu và đạo hàm tại biên.
    
    Args:
    points (np.ndarray): Mảng các điểm dữ liệu, mỗi điểm là một cặp [x, y].
    fpa (float): Đạo hàm tại điểm đầu tiên.
    fpb (float): Đạo hàm tại điểm cuối cùng.
    
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

    # Điều kiện biên spline kẹp
    A[0, 0] = 2 * h[0]
    A[0, 1] = h[0]
    A[-1, -2] = h[-1]
    A[-1, -1] = 2 * h[-1]
    b[0] = 3 * (alpha[0] - fpa)
    b[-1] = 3 * (fpb - alpha[-1])

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

# Dữ liệu điểm từ bài tập 3
points_a = np.array([[8.3, 17.56492], [8.6, 18.50515]], dtype=float)
points_b = np.array([[0.8, 0.22363362], [1.0, 0.65809197]], dtype=float)
points_c = np.array([[-0.5, -0.0247500], [-0.25, 0.3349375], [0, 1.1010000]], dtype=float)
points_d = np.array([[0.1, -0.62049958], [0.2, -0.28398668], [0.3, 0.00660095], [0.4, 0.24842440]], dtype=float)

# Hệ số spline bậc ba cho mỗi đoạn
coefficients_a = cubic_spline(points_a, 3.116256, 3.151762)
coefficients_b = cubic_spline(points_b, 2.1691753, 2.0466965)
coefficients_c = cubic_spline(points_c, 0.7510000, 4.0020000)
coefficients_d = cubic_spline(points_d, 3.58502082, 2.16529366)

print("Hệ số spline bậc ba cho mỗi đoạn (câu a):")
for i, coeff in enumerate(coefficients_a):
    print(f"Đoạn {i}: a={coeff[0]}, b={coeff[1]}, c={coeff[2]}, d={coeff[3]}")

print("\nHệ số spline bậc ba cho mỗi đoạn (câu b):")
for i, coeff in enumerate(coefficients_b):
    print(f"Đoạn {i}: a={coeff[0]}, b={coeff[1]}, c={coeff[2]}, d={coeff[3]}")

print("\nHệ số spline bậc ba cho mỗi đoạn (câu c):")
for i, coeff in enumerate(coefficients_c):
    print(f"Đoạn {i}: a={coeff[0]}, b={coeff[1]}, c={coeff[2]}, d={coeff[3]}")

print("\nHệ số spline bậc ba cho mỗi đoạn (câu d):")
for i, coeff in enumerate(coefficients_d):
    print(f"Đoạn {i}: a={coeff[0]}, b={coeff[1]}, c={coeff[2]}, d={coeff[3]}")

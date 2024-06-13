import numpy as np
import scipy.linalg as sla

def cubic_spline(points, f_prime_0, f_prime_n):
    """
    Tính các hệ số cho phép nội suy spline bậc ba từ một tập hợp các điểm dữ liệu và điều kiện biên clamped.
    
    Args:
    points (np.ndarray): Mảng các điểm dữ liệu, mỗi điểm là một cặp [x, y].
    f_prime_0 (float): Giá trị đạo hàm tại điểm đầu tiên.
    f_prime_n (float): Giá trị đạo hàm tại điểm cuối cùng.
    
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

    # Điều kiện biên clamped
    A[0, 0] = 2 * h[0]  # Hệ số cho điều kiện biên đầu tiên
    A[0, 1] = h[0]  # Hệ số cho điều kiện biên đầu tiên
    b[0] = 3 * (alpha[0] - f_prime_0)  # Vế phải phương trình cho điều kiện biên đầu tiên

    A[-1, -1] = 2 * h[-1]  # Hệ số cho điều kiện biên cuối cùng
    A[-1, -2] = h[-1]  # Hệ số cho điều kiện biên cuối cùng
    b[-1] = 3 * (f_prime_n - alpha[-1])  # Vế phải phương trình cho điều kiện biên cuối cùng

    for i in range(1, n):
        A[i, i - 1] = h[i - 1]  # Hệ số cho phương trình thứ i
        A[i, i] = 2 * (h[i - 1] + h[i])  # Hệ số cho phương trình thứ i
        A[i, i + 1] = h[i]  # Hệ số cho phương trình thứ i
        b[i] = 3 * (alpha[i] - alpha[i - 1])  # Vế phải phương trình thứ i

    # Bước 3: Giải hệ phương trình tuyến tính cho c
    c = sla.solve(A, b)  # Giải hệ phương trình tuyến tính để tìm các hệ số c

    # Bước 4: Tính b, d và gán a
    d = np.diff(c) / (3 * h)  # Tính các hệ số d
    b = alpha - h * (2 * c[:-1] + c[1:]) / 3  # Tính các hệ số b
    a = y[:-1]  # Gán các hệ số a từ y

    # Mỗi hàng trong coeffs tương ứng với [a, b, c, d] cho mỗi đoạn
    coeffs = np.vstack([a, b, c[:-1], d]).T  # Tạo mảng chứa các hệ số

    return coeffs

# Dữ liệu và điều kiện biên cho bài 8

# Câu a
points_a = np.array([[0.0, 1.0000], [0.5, 2.71828]], dtype=float)
coefficients_a = cubic_spline(points_a, 2, 5.43656)
print("Hệ số spline bậc ba cho mỗi đoạn (câu a):")
for i, coeff in enumerate(coefficients_a):
    print(f"Đoạn {i}: a={coeff[0]}, b={coeff[1]}, c={coeff[2]}, d={coeff[3]}")

# Câu b
points_b = np.array([[-0.25, 1.33203], [0.25, 0.800781]], dtype=float)
coefficients_b = cubic_spline(points_b, 0.437500, -0.625000)
print("Hệ số spline bậc ba cho mỗi đoạn (câu b):")
for i, coeff in enumerate(coefficients_b):
    print(f"Đoạn {i}: a={coeff[0]}, b={coeff[1]}, c={coeff[2]}, d={coeff[3]}")

# Câu c
points_c = np.array([[0.1, -0.2904996], [0.2, -0.56079734], [0.3, -0.81401972]], dtype=float)
coefficients_c = cubic_spline(points_c, -2.8004996, -2.9734038)
print("Hệ số spline bậc ba cho mỗi đoạn (câu c):")
for i, coeff in enumerate(coefficients_c):
    print(f"Đoạn {i}: a={coeff[0]}, b={coeff[1]}, c={coeff[2]}, d={coeff[3]}")

# Câu d
points_d = np.array([[-1.0, 0.86199480], [-0.5, 0.95802009], [0.0, 1.0986123], [0.5, 1.2943767]], dtype=float)
coefficients_d = cubic_spline(points_d, 0.15536240, 0.45186276)
print("Hệ số spline bậc ba cho mỗi đoạn (câu d):")
for i, coeff in enumerate(coefficients_d):
    print(f"Đoạn {i}: a={coeff[0]}, b={coeff[1]}, c={coeff[2]}, d={coeff[3]}")

import numpy as np
import scipy.linalg as sla
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

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
    A[0, 0] = 1  # Đặt điều kiện biên đầu tiên cho spline tự nhiên
    A[-1, -1] = 1  # Đặt điều kiện biên cuối cùng cho spline tự nhiên

    for i in range(1, n):
        A[i, i - 1] = h[i - 1]  # Hệ số cho h[i-1]
        A[i, i] = 2 * (h[i - 1] + h[i])  # Hệ số cho 2*(h[i-1] + h[i])
        A[i, i + 1] = h[i]  # Hệ số cho h[i]
        b[i] = 3 * (alpha[i] - alpha[i - 1])  # Hệ số cho 3*(alpha[i] - alpha[i-1])

    # Bước 3: Giải hệ phương trình tuyến tính cho c
    c = sla.solve(A, b)  # Giải hệ phương trình để tìm các hệ số c

    # Bước 4: Tính b, d và gán a
    d = np.diff(c) / (3 * h)  # Tính hệ số d
    b = alpha - h * (2 * c[:-1] + c[1:]) / 3  # Tính hệ số b
    a = y[:-1]  # Hệ số a là giá trị y tại các điểm

    # Mỗi hàng trong coeffs tương ứng với [a, b, c, d] cho mỗi đoạn
    coeffs = np.vstack([a, b, c[:-1], d]).T  # Kết hợp các hệ số thành một mảng

    return coeffs  # Trả về mảng hệ số

# Dữ liệu điểm từ bài tập 29
time_points = np.array([0, 3, 5, 8, 13])  # Thời gian (giây)
distance_points = np.array([0, 225, 383, 623, 993])  # Khoảng cách (feet)
speed_points = np.array([75, 77, 80, 74, 72])  # Vận tốc (feet/giây)

# Tạo spline bậc ba khép kín cho khoảng cách và vận tốc
distance_spline = CubicSpline(time_points, distance_points, bc_type='clamped')
speed_spline = CubicSpline(time_points, speed_points, bc_type='clamped')

# Xấp xỉ vị trí và vận tốc của xe khi t = 10 giây
t = 10
approx_distance = distance_spline(t)  # Vị trí của xe
approx_speed = speed_spline(t)  # Vận tốc của xe

print(f"Vị trí ước lượng của xe tại t = {t} giây: {approx_distance:.2f} feet")
print(f"Vận tốc ước lượng của xe tại t = {t} giây: {approx_speed:.2f} feet/giây")

# Kiểm tra xem xe có bao giờ vượt quá giới hạn tốc độ 55 dặm/giờ (55 mi/h = 55 * 5280 feet / 3600 giây = 80.67 feet/giây)
speed_limit = 80.67  # Giới hạn tốc độ
exceeds_speed_limit = np.any(speed_spline(time_points) > speed_limit)
first_exceed_time = None
if exceeds_speed_limit:
    for time in np.linspace(0, 13, 1000):
        if speed_spline(time) > speed_limit:
            first_exceed_time = time
            break

print(f"Xe có bao giờ vượt quá giới hạn tốc độ 55 mi/h không? {'Có' if exceeds_speed_limit else 'Không'}")
if exceeds_speed_limit:
    print(f"Thời điểm đầu tiên xe vượt quá giới hạn tốc độ là: {first_exceed_time:.2f} giây")

# Tính tốc độ tối đa dự đoán của xe
max_speed = np.max(speed_spline(time_points))
print(f"Tốc độ tối đa dự đoán của xe: {max_speed:.2f} feet/giây")

# Vẽ đồ thị spline
plt.figure(figsize=(10, 6))

# Đồ thị khoảng cách
plt.subplot(2, 1, 1)
plt.plot(time_points, distance_points, 'o', label='Dữ liệu thực tế (khoảng cách)')
plt.plot(np.linspace(0, 13, 100), distance_spline(np.linspace(0, 13, 100)), label='Spline bậc ba khép kín (khoảng cách)')
plt.xlabel('Thời gian (giây)')
plt.ylabel('Khoảng cách (feet)')
plt.legend()
plt.title('Nội suy spline bậc ba khép kín cho khoảng cách của xe')

# Đồ thị vận tốc
plt.subplot(2, 1, 2)
plt.plot(time_points, speed_points, 'o', label='Dữ liệu thực tế (vận tốc)')
plt.plot(np.linspace(0, 13, 100), speed_spline(np.linspace(0, 13, 100)), label='Spline bậc ba khép kín (vận tốc)')
plt.axhline(speed_limit, color='r', linestyle='--', label='Giới hạn tốc độ 55 mi/h')
plt.xlabel('Thời gian (giây)')
plt.ylabel('Vận tốc (feet/giây)')
plt.legend()
plt.title('Nội suy spline bậc ba khép kín cho vận tốc của xe')

plt.tight_layout()
plt.show()

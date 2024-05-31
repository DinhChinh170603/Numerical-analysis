import numpy as np

# Dữ liệu điểm
x = np.array([4.0, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1])
y = np.array([102.56, 113.18, 130.11, 142.05, 167.53, 195.14, 224.87, 256.73, 299.50, 326.72])

def augmented_matrix_cal(x: np.ndarray, y: np.ndarray, degree=2, discrete=True):
    """
    Tính ma trận augmented cho phương pháp bình phương tối thiểu.
    
    Args:
    x (np.ndarray): Mảng các giá trị x.
    y (np.ndarray): Mảng các giá trị y.
    degree (int): Bậc của đa thức.
    discrete (bool): Chế độ tính toán (discrete hay không).
    
    Returns:
    tuple: Ma trận hệ số và các biến phụ thuộc.
    """
    coefficient = np.empty([degree + 1, degree + 1])  # Khởi tạo ma trận hệ số

    if discrete:
        # Tạo ma trận Vandermonde để tính toán
        V = np.vander(x, degree * 2 + 1, increasing=True)

        # Lấy các giá trị hệ số
        coefficienct_values = np.sum(V, axis=0)

        # Gán giá trị vào ma trận hệ số
        for i in range(degree + 1):
            coefficient[i] = coefficienct_values[i: i + degree + 1]

        x_pow_n_values = V[:, :degree + 1]
        dependent_vars = np.dot(y, x_pow_n_values)  # Tính các biến phụ thuộc
        
    else:
        return None

    return coefficient, dependent_vars

# Tính ma trận augmented
coefficients, dependent_vars = augmented_matrix_cal(x, y, 3)

# Giải hệ phương trình bằng phương pháp bình phương tối thiểu
result, _, _, _ = np.linalg.lstsq(coefficients, dependent_vars, rcond=None)

print("Hệ số của đa thức nội suy:")
print(result)

import numpy as np
from numpy.linalg import inv, norm

def inverse_iteration(A, x0, tol=1e-10, max_iter=1000):
    """
    Phương pháp Inverse Iteration để tìm gtri riêng nhỏ nhất và vecto riêng tương ứng.
    :param A: Ma trận vuông
    :param x0: Vector khởi tạo ban đầu
    :param tol: Ngưỡng sai số
    :param max_iter: Số lần lặp tối đa
    :return: Eigenvalue nhỏ nhất và eigenvector tương ứng
    """
    x = x0 / norm(x0)  # Chuẩn hóa vector ban đầu
    I = np.eye(A.shape[0])  # Ma trận đơn vị
    eigenvalue = None

    for k in range(max_iter):
        y = np.dot(inv(A), x)  # Giải hệ phương trình Ay = x
        mu = np.dot(x.T, y)  # Tính gtri riêng
        x = y / norm(y)  # Chuẩn hóa vecto riêng
        eigenvalue = mu

        # Kiểm tra ngưỡng sai số
        if norm(np.dot(A, x) - mu * x) < tol:
            return eigenvalue, x

    print("Số lần lặp tối đa đã vượt quá")
    return eigenvalue, x

# Ví dụ sử dụng Inverse Iteration
A = np.array([[4, 1],
              [2, 3]])

x0 = np.random.rand(A.shape[0])  # Vector khởi tạo ngẫu nhiên

eigenvalue, eigenvector = inverse_iteration(A, x0)

print(f"Giá trị riêng nhỏ nhất: {eigenvalue}")
print(f"Vector riêng tương ứng: {eigenvector}")

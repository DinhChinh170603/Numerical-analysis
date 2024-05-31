import numpy as np
from numpy.linalg import norm

def normalize(A: np.ndarray, b: np.ndarray):
    """ Chuẩn hóa ma trận A để phần tử trên đường chéo là 1. """
    n = len(A)
    for i in range(n):
        div = A[i][i]
        A[i] = A[i] / div  # Chuẩn hóa hàng i của A
        b[i] = b[i] / div  # Chuẩn hóa phần tử thứ i của vector b
    return A, b

def gauss_seidel(A: np.ndarray, b: np.ndarray, max_iter=1000, tol=1e-5):
    """ Phương pháp lặp Gauss-Seidel để giải hệ phương trình Ax = b. """
    n = len(A)
    x = np.zeros(n)  # Khởi tạo giá trị ban đầu cho x
    
    # Lặp cho đến khi đạt đủ số lần lặp max_iter hoặc sai số dưới ngưỡng tol
    for _ in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            s1 = np.dot(A[i, :i], x[:i])  # Tổng phần tử trước i
            s2 = np.dot(A[i, i+1:], x[i+1:])  # Tổng phần tử sau i
            x_new[i] = (b[i] - s1 - s2) / A[i, i]  # Cập nhật x[i] theo công thức Gauss-Seidel
        
        # Kiểm tra điều kiện dừng
        if norm(x_new - x, np.inf) < tol:
            return x_new
        
        x = x_new
    
    raise ValueError("Không hội tụ sau {} lần lặp".format(max_iter))

# Ví dụ sử dụng
if __name__ == "__main__":
    A = np.array([[4, 1, 0], [1, 4, 1], [0, 1, 4]], dtype=float)
    b = np.array([1, 2, 3], dtype=float)
    print("Nghiệm x:", gauss_seidel(A, b))

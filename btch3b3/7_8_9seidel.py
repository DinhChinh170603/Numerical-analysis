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

# Giải các hệ phương trình trong bài tập 7, 8 và 9
if __name__ == "__main__":
    # Bài tập 7
    A7 = np.array([[5, -2, 0],
                   [-2, 10, -2],
                   [0, -2, 15]], dtype=float)
    b7 = np.array([18, -60, 128], dtype=float)
    print("Bài tập 7 - Nghiệm x:", gauss_seidel(A7, b7))

    # Bài tập 8
    A8 = np.array([[3, 2, 1],
                   [1, 3, 2],
                   [2, 1, 3]], dtype=float)
    b8 = np.array([7, 4, 7], dtype=float)
    print("Bài tập 8 - Nghiệm x:", gauss_seidel(A8, b8))

    # Bài tập 9
    A9 = np.array([[5, 1, 2],
                   [1, 4, -2],
                   [2, 3, 8]], dtype=float)
    b9 = np.array([19, -2, 39], dtype=float)
    print("Bài tập 9 - Nghiệm x:", gauss_seidel(A9, b9))

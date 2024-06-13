import numpy as np
from numpy import matmul
from numpy.linalg import inv
import scipy.linalg

# Khai báo hàm nhập ma trận, dù không được sử dụng trong đoạn code mẫu này.
def text_input(matrix):
    return matrix

# Hàm thực hiện phân tích LU và giải hệ phương trình Ax = b
def LU_factorization(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    # Phân tách ma trận A thành L (lower triangular) và U (upper triangular) sử dụng scipy
    _, L, U = scipy.linalg.lu(A)

    # In ma trận A
    print("A:")
    print(np.matrix(A))

    # In kết quả phân tách L và U
    print('\nfactorization:')
    print("L:")
    print(np.matrix(L))
    print("U:")
    print(np.matrix(U))

    # Tính vector y bằng cách giải phương trình Ly = b, sử dụng nghịch đảo của L
    y = matmul(inv(L), b)
    print('\ny = L^-1 * b =')
    print(y)

    # Tính vector x bằng cách giải phương trình Ux = y, sử dụng nghịch đảo của U
    x = matmul(inv(U), y)
    print('\nx = U^-1 * y =')
    print(x.flatten())
    return x.flatten()

# Đoạn code chính để thử nghiệm hàm
if __name__ == "__main__":
    # Bài tập 7
    A7 = np.array([[9, 6, 12],
                   [6, 13, 11],
                   [12, 11, 26]], dtype=float)
    b7 = np.array([17.4, 23.6, 30.8], dtype=float).reshape(-1, 1)
    print("Bài tập 7:")
    LU_factorization(A7, b7)
    print("\n--------------------------\n")

    # Bài tập 8
    A8 = np.array([[4, 6, 8],
                   [6, 34, 52],
                   [8, 52, 129]], dtype=float)
    b8 = np.array([0, -160, -452], dtype=float).reshape(-1, 1)
    print("Bài tập 8:")
    LU_factorization(A8, b8)
    print("\n--------------------------\n")

    # Bài tập 9
    A9 = np.array([[0.01, 0, 0.03],
                   [0, 0.16, 0.08],
                   [0.03, 0.08, 0.14]], dtype=float)
    b9 = np.array([0.14, 0.16, 0.54], dtype=float).reshape(-1, 1)
    print("Bài tập 9:")
    LU_factorization(A9, b9)

import numpy as np
from numpy import matmul
from numpy.linalg import inv
import scipy.linalg


# matrix
# A = np.array([[7, 3, -2, 2], [3, 8, 1, -4],
#                 [-1, 1, 4, -2], [2, -3, -1, 6]])
# b = np.array([[1], [2], [3], [4]])

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

    #inv là hàm nghịch đảo

    # Tính vector y bằng cách giải phương trình Ly = b, sử dụng nghịch đảo của L
    y = matmul(inv(L), b)
    print('\ny = U * x = L^-1 * b =')
    print(inv(L))

    # Tính vector x bằng cách giải phương trình Ux = y, sử dụng nghịch đảo của U
    x = matmul(inv(U), y)
    print('\nx = U^-1 * y =')
    print(x.flatten())
    return x.flatten()

# Đoạn code chính để thử nghiệm hàm
if __name__ == "__main__":
    # Giả sử A và b đã được định nghĩa ở đâu đó trước đoạn này
    LU_factorization(A, b)
import numpy as np
from numpy import matmul
from numpy.linalg import inv
import scipy.linalg


# matrix
# A = np.array([[7, 3, -1, 2], [3, 8, 1, -4],
#                 [-1, 1, 4, -1], [2, -4, -1, 6]])
# b = np.array([[1], [4], [2], [3]])

def text_input(matrix):
    return matrix

def LU_factorization(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    _, L, U = scipy.linalg.lu(A)

    print("A:")
    print(np.matrix(A))

    print('\nfactorization:')
    print("L:")
    print(np.matrix(L))

    print("U:")
    print(np.matrix(U))

    y = matmul(inv(L), b)
    print('\ny = U * x = L^-1 * b =')
    print(inv(L))


    x = matmul(inv(U), y)
    print('\nx = U^-1 * y =')
    print(x.flatten())
    return x.flatten()


if __name__ == "__main__":

    LU_factorization(A, b)
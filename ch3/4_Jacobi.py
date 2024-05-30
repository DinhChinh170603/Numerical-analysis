import numpy as np
from numpy.linalg import inv, norm

def normalize(A: np.ndarray, b: np.ndarray):
    for i in range(len(A)):
        div = A[i][i]
        for j in range(len(A)):
            A[i][j] = A[i][j] / div
        b[i][0] /= div

    return A, b

def jacobi_iteartion(A: np.ndarray, b: np.ndarray, TOL=1e-3, max_iteration=1000):
    # step 1
    A, b = normalize(A, b)

    # step 2
    I = np.identity(len(A))
    C = I + (-A)

    if norm(C, np.inf) >= 1:
        print('not convergence')
        return

    print("C = I - A: \n", C)

    x0 = b
    for _ in range(max_iteration):
        x = b + np.matmul(C, x0)
        if (norm(x-x0) < TOL):
            return x.flatten()
        x0 = x

    if i > max_iteration:
        print(f'excessed {i} iteration')

    return x.flatten()


def solve(A, b):
    """
    Convert 2d list A into a 2d array with diagonal full of 1.
    """
    for i in range(len(A)):
        div = A[i][i]
        for j in range(len(A)):
            A[i][j] = A[i][j] / div
        b[i][0] /= div
    print("A = \n", np.array(A))
    print("b =\n", np.array(b))

    x0 = np.zeros_like(b)

    return jacobiMethod(np.array(A), x0, np.array(b))


if __name__ == "__main__":

    print("Exercise 8.")

    problems = [
        # # a
        # ([
        #     [4, 1, -1],
        #     [-1, 3, 1],
        #     [2, 2, 5]],
        #     [[5], [-4], [1]]),
        # # b
        # ([
        #     [-2, 1, 0.5],
        #     [1, -2, -0.5],
        #     [0, 1, 2]],
        #     [[4], [-4], [0]]),
        # # c
        # ([
        #     [4, 1, -1, 1],
        #     [1, 4, -1, -1],
        #     [-1, -1, 5, 1],
        #     [1, -1, 1, 3]],
        #     [[-2], [-1], [0], [1]]),
        # # d
        # ([[4, -1, 0, -1, 0, 0],
        #     [-1, 4, -1, 0, -1, 0],
        #     [0, -1, 4, 0, 0, -1],
        #     [-1, 0, 0, 4, -1, 0],
        #     [0, -1, 0, -1, 4, -1],
        #     [0, 0, -1, 0, -1, 4]],
        #  [[0], [5], [0], [6], [-2], [-6]]),
        #
        # ([[4, 1, -1],
        #  [-1, 3, 1],
        #     [2, 2, 5]],
        #  [[5], [-4], [1]])
        ([[9, -3, -3],
          [-3, 10, 1],
          [-3, 1, 5]],
         [[-9], [-1.5], [5]])

    ]

    for i in range(len(problems)):
        print("\n", chr(ord('a') + i),
              "----------------------------------------------------------")
        A, b = problems[i]
        print("Solution x =", solve(A, b))

    # print(mGaussSeidel(A, b, TOL))
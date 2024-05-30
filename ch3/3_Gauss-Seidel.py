import numpy as np
from numpy.linalg import inv, norm

def normalize(A: np.ndarray, b: np.ndarray):
    for i in range(len(A)):
        div = A[i][i]
        for j in range(len(A)):
            A[i][j] /= div
        b[i][0] /= div

    return A, b

def gauss_scidel_iteration(A: np.ndarray, b: np.ndarray, max_iteration, TOL= 1e-3) -> np.ndarray:

    # step 1 + 2
    A, b = normalize(A, b)

    # step 3
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    I = np.identity(len(A))


    # step 4
    print('A = L + I + U')
    print("L = \n", L.tolist())
    print("U = \n", U.tolist())
    print("I = \n", I.tolist())

    # step 5
    C = -np.matmul(inv(I + L), U)
    d = np.matmul(inv(I + L), b)

    if norm(C, np.inf) >= 1:
        print('not convergence')
        return
    
    print('C:')
    print(C.tolist())
    print('d:')
    print(d.tolist())



    # step 6
    i = 1
    x0 = d
    while i <= max_iteration:
        x = np.matmul(C, x0) + d
        if norm(x-x0) < TOL:
            return x.flatten()
        x0 = x

    if i > max_iteration:
        print(f'excessed {i} iteration')

    return x.flatten()
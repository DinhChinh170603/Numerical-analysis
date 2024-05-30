import numpy as np
import math

# function to subtitute
p = lambda x: x
q = lambda x: x * 2
r = lambda x: x + 3

def func1(x, y: np.ndarray):
    res = np.ndarray(1)

    res[0] = p(x) * y[0] + q[x] * y[1] + r(x)

    return res

def func2(x, y: np.ndarray):
    res = np.ndarray(1)

    res[0] = p(x) * y[0] + q[x] * y[1]

    return res

def RK4(df, x, y: np.array, h):
    k1 = df(x, y)

    k2 = df(x + 0.5 * h, y + 0.5 * h * k1)

    k3 = df(x + 0.5 * h, y + 0.5 * h * k2)

    k4 = df(x + h, y + h * k3)

    y1 = y + h/6 * (k1 + 2 * k2 + 2 * k3 + k4)

    return y1

def linear_shooting(a, b, alpha, beta, N, TOL):
    
    # step 1
    h = (b - a) / N

    u = np.ndarray([alpha, 0])
    v = np.ndarray([0, 1])

    # step 2
    i = 0
    while i < N:
        x = a + i * h

        # step 3 + 4 using RK4
        u = RK4(func1, x, u, h)

        v = RK4(func2, x, v, h)

    # step 5
    w1 = alpha
    w2 = (beta - u) / v
    print(f'a; w1, w2 initial:')
    print(a, w1, w2, sep='\n')

    # step 6
    i = 1
    for i in range(N):
        W1 = u


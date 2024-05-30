import numpy as np
import math

# hệ ptvp
def df(x, y: np.array):
    # number of equations
    res = np.ndarray(2)

    res[0] = 1/9 * y[0] - 2/3 * y[1] + 1 / 9 * x ** 2 + 2/3
    res[1] = y[1] + 3 * x - 4

    return res

def _actual(x):
    res = np.ndarray(2)

    res[0] = -3 * math.e ** x + x ** 2
    res[1] = 4 * math.e ** x - 3 * x + 1

    return res

def RK4(x, y: np.array, h):
    k1 = df(x, y)

    k2 = df(x + 0.5 * h, y + 0.5 * h * k1)

    k3 = df(x + 0.5 * h, y + 0.5 * h * k2)

    k4 = df(x + h, y + h * k3)

    y1 = y + h/6 * (k1 + 2 * k2 + 2 * k3 + k4)

    return y1

def main():

    # điều kiện
    t = 0
    y = np.array([-3, 5])
    h = 0.2
    iteration = 10

    print('RK4 differential equation(s):')
    for i in range(iteration):
        print(f'điểm mốc thứ {i + 1}')

        y1 = RK4(t, y, h)

        print(f'u1 = {round(y1[0], 10)}, u2 = {round(y1[1], 10)}')

        y = y1
        t = round(i * h + h, 3)
    print(f'\nthực tế: {_actual(2)}')
    print(f'sai số: {y -  _actual(2)}')

main()
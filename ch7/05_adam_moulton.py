import math
import numpy as np

# bai 1 c

# hệ ptvp
def df(x, y: np.array):
    # number of equations
    res = np.ndarray(1)

    res[0] = 1 + y[0] / x

    return res

def _actual(x):
    res = np.ndarray(1)
    
    res[0] = x * np.log(x) + 2 * x

    return res

def RK4(x, y: np.array, h):
    k1 = df(x, y)

    k2 = df(x + 0.5 * h, y + 0.5 * h * k1)

    k3 = df(x + 0.5 * h, y + 0.5 * h * k2)

    k4 = df(x + h, y + h * k3)

    y1 = y + h/6 * (k1 + 2 * k2 + 2 * k3 + k4)

    return y1

def adam_moulton(x, y :list, h, step=2):
    if step == 1:
        y0 = y[0]
        return RK4(x, y0, h)
    
    if step == 2:
        y0, y1 = y[-2:]

        _predictor = y1 + h * (3 / 2 * df(x, y1) - 1 / 2 * df(x - h, y0))
        _corrector = y1 + h * (1 / 2 * df(x + h, _predictor) + 1 / 2 * df(x, y0))
        

        return _corrector
    
    if step == 3:
        
        y0, y1, y2 = y[-3:]

        _predictor = y2 + h * (23 / 12 * df(x, y2) - 16 / 12 * df(x - h, y1) + 5 / 12 * df(x - 2 * h, y0))
        _corrector = y2 + h * (5 / 12 * df(x + h, _predictor) + 8 / 12 * df(x, y2) -1 / 12 * df(x - h, y1))

        return _corrector

    if step > 3:
        y0, y1, y2, y3 = y[-4:]
        
        _predictor = y3 + h / 24 * (55 * df(x, y3) - 59 * df(x - h, y2) + 37 * df(x - 2 * h, y1) - 9 * df(x - 3 * h, y0))
        _corrector = y3 + h / 24 * (9 * df(x + h, _predictor) + 19 * df(x, y3) - 5 * df(x - h, y2) + df(x - 2 * h, y1))

        return _corrector
    
def main():
    print('Adam Mouton:')

    h = 0.2
    x = 1
    y = np.array([2])

    step = 0

    y_list = [y]

    while x < 2:
        step = step + 1

        print(f'\niteration {step}: ')
        y_temp = adam_moulton(x, y_list, h, step)
        print(f'x = {x + h}\ny = {y_temp[0]}')
        print(f'actual: y = {_actual(x + h)}')
        y_list.append(y_temp)
        print(f'error = {y_temp[0] - _actual(x + h)}')
        x = round(x + h, 6)

main()
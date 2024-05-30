import numpy as np
import math

x0 = 1
y0 = -4
h = 0.01

# base derivative function
def func(x):
    return 1 + x ** 2

# symetric derivatives for better number approximation
def df(func, x, order = 1):
    h = 1e-5

    if order > 1:
        return (df(func, x + h, order - 1) - df(func, x - h, order - 1)) / (2 * h)
    
    # return (func(x + h) - func(x - h)) / (2 * h)
    return func(x)

def taylor_series(x: float, y, h, iteration, order = 1):
    if order == 1:
        print("Newton method.")
    else:
        print("Taylor series method.")

    for i in range(iteration):
        print(f'iteration {i}')

        temp = y
        # high order taylor series
        for j in range(1, order + 1):
            temp += h**j / math.factorial(j) * df(func, x, j)

        print(f'x = {x}')
        print(f'y = {y}')
        y = temp
        x = x + h

taylor_series(x0, y0, h, 4, 1)
        

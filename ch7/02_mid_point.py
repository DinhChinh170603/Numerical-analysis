import math

h = 0.1
x0 = 0
y0 = 1 / 3

def func(x, y):
    return -5 * y + 5 * x ** 2 + 2 * x

def mid_point(x, y, h, iteration):
    print("Mid point method:")

    for i in range(iteration):
        print(f'iteration {i + 1}')

        # mid point
        x_mid = x + h * 0.5
        y_mid = y + h * 0.5 * func(x, y)
        
        # final point
        y = y + h * func(x_mid, y_mid)

        print(f'x = {x}')
        print(f'y = {y}')

        x = x + h



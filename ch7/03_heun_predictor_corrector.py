import math

h = 0.1
x = 0
y = 1 / 3

def func(x, y):
    return -5 * y + 5 * x ** 2 + 2 * x

def predictor(x, y, h):
    return y + h * func(x, y)

def corrector(x, y, h, pred):
    return y + h / 2 * (func(x, y) + func(x, pred))

def actual(x):
    return x ** 2 + 1 / 3 * math.e ** (-5 * x)

def mid_point(x, y, h, iteration):
    print("Heun's predictor corrector method:")

    for i in range(iteration):
        print(f'iteration {i + 1}')

        # predictor and corrector
        _pred = predictor(x, y, h)
        print(f'predictor: {_pred}')
        _correct = corrector(x, y, h, _pred)
        print(f'corrector: {_correct}')

        # error
        print(f'actual value: y = {actual(x + h)}')
        print(f'error: {abs(y - actual(x))}')
        
        y = _correct
        x = x + h
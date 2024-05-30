import math

a = 0
b = math.pi

def func_g(x):
    return pow((x + 3) / (x ** 2 + 2) , 1/2)

def fix_point(p_0, tolerance, max_iteration):
    print('iteration\t\tp\t\t\tf(p)\t\t\t\ttol')
    
    # initial i
    i = 1

    while i <= max_iteration:
        p = func_g(p_0)
        if abs(p - p_0) < tolerance:
            print(f'final p:{p}')
            return
        
        print(f'{i}\t\t\t{p}\t{func_g(p)}\t{abs(p_0 - p)}')
        
        i += 1
        p_0 = p


fix_point(1, 10 ** -5, 100)
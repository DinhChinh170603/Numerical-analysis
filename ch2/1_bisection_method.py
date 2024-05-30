import math

# function
def func(x):
    return x** 2 - 3

# endpoint
a = 1.7
b = 1.8

# other params
TOL = 1e-5
max_iteration = 1e6

'''
input: Function f, 
       endpoint values a, b, 
       tolerance TOL, 
       maximum iterations NMAX
conditions: a < b, 
            either f(a) < 0 and f(b) > 0 or f(a) > 0 and f(b) < 0
output: value which differs from a root of f(x) = 0 by less than TOL
 
N ← 1
while N ≤ NMAX do // limit iterations to prevent infinite loop
    c ← (a + b)/2 // new midpoint
    if f(c) = 0 or (b – a)/2 < TOL then // solution found
        Output(c)
        Stop
    end if
    N ← N + 1 // increment step counter
    if sign(f(c)) = sign(f(a)) then a ← c else b ← c // new interval
end while
Output("Method failed.") // max number of steps exceeded
'''

def bisection_method(a, b, TOL, max_iteration):

    i = 1
    FA = func(a)

    while i <= max_iteration:
        print(f'vòng lặp thứ {i}: ')
        p = a + (b - a) / 2
        FP = func(p)
        print(f'p = {p}, f(p) = {FP}')

        if FP == 0 or (b - a) / 2 < TOL:
            print(f'kết quả: p = {p}, f(p) = {FP}')
            return
        
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p

        
        i = i + 1

    print(f'thất bại sau {i} vòng lặp')

bisection_method(a, b, TOL, max_iteration)


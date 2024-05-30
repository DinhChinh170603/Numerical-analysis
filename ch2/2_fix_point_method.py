import math

# function
def g(x):
    return x** 2 - 3

# params
p0 = 100
TOL = 1e-5
max_iteration = 1e6

'''
INPUT initial approximation p0; tolerance TOL; maximum number of iterations N0.
OUTPUT approximate solution p or message of failure.
Step 1 Set i = 1.
Step 2 While i ≤ N0 do Steps 3–6.
    Step 3 Set p = g( p0). (Compute pi.)
    Step 4 If | p − p0| < TOL then
        OUTPUT ( p); (The procedure was successful.)
        STOP.
    Step 5 Set i = i + 1.
    Step 6 Set p0 = p. (Update p0.)
Step 7 OUTPUT (‘The method failed after N0 iterations, N0 =’, N0);
    (The procedure was unsuccessful.)
    STOP.
'''

def fixpoint_method(p0, TOL, max_iteration):

    i = 1

    while i <= max_iteration:
        print(f'vòng lặp thứ {i}: ')
        p = g(p0)
        print(f'p = {p0}, f(p) = {p}')
        
        if abs(p0 - p) <= TOL:
            print(f'kết quả: p = {p}')
            return
        
        p0 = p
        i = i + 1

    print(f'thất bại sau {i} vòng lặp')

fixpoint_method(p, TOL, max_iteration)
def func(x):
    return x ** 2 - 6

def diff_func(x):
    return (func(x + 1e-9) - func(x)) / (1e-9) 

# params
p0 = 1
TOL = 1e-6
max_iteration = 1e6

'''
INPUT initial approximation p0; tolerance TOL; maximum number of iterations N0.
OUTPUT approximate solution p or message of failure.
Step 1 Set i = 1.
Step 2 While i ≤ N0 do Steps 3–6.
    Step 3 Set p = p0 − f ( p0)/f ( p0). (Compute pi.)
    Step 4 If | p − p0| < TOL then
        OUTPUT (p); (The procedure was successful.)
        STOP.
    Step 5 Set i = i + 1.
    Step 6 Set p0 = p. (Update p0.)
Step 7 OUTPUT (‘The method failed after N0 iterations, N0 =’, N0);
    (The procedure was unsuccessful.)
    STOP.
'''
def newton_method(p0, TOL, max_iteration):
    i = 1

    while i <= max_iteration:
        p = p0 - func(p0) / diff_func(p0)

        if abs(p - p0) < TOL:
            print(f'kết quả: p = {p}')
            return
        
        i+=1
        p0 = p

    
    print(f'thất bại sau {i} vòng lặp')
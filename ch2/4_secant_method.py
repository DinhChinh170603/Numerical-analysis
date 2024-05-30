def func(x):
    return x ** 2 - 6

# params
p0 = 3
p1 = 2
TOL = 1e-6
max_iteration = 1e6

'''
INPUT initial approximations p0, p1; tolerance TOL; maximum number of iterations N0.
OUTPUT approximate solution p or message of failure.
Step 1 Set i = 2;
    q0 = f ( p0);
    q1 = f ( p1).
Step 2 While i ≤ N0 do Steps 3–6.
    Step 3 Set p = p1 − q1( p1 − p0)/(q1 − q0). (Compute pi.)
    Step 4 If | p − p1| < TOL then
        OUTPUT (p); (The procedure was successful.)
        STOP.
    Step 5 Set i = i + 1.
    Step 6 Set p0 = p1; (Update p0, q0, p1, q1.)
        0 = q1;
        p1 = p;
        q1 = f ( p).
Step 7 OUTPUT (‘The method failed after N0 iterations, N0 =’, N0);
    (The procedure was unsuccessful.)
    STOP.
'''
def secant_method(p0, p1,  TOL, max_iteration):
    i = 2
    q0 = func(p0)
    q1 = func(p1)

    while i <= max_iteration:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)

        if abs(p - p1) < TOL:
            print(f'kết quả: p = {p}')
            return
        
        p0 = p1
        q0 = q1
        p1 = p
        q1 = func(p)

        i+=1

    print(f'thất bại sau {i} vòng lặp')
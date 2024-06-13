import math

def f(h):
    L = 10
    r = 1
    V = 12.4
    return L * (0.5 * math.pi * r**2 - r**2 * math.asin(h/r) - h * (r**2 - h**2)**0.5) - V

def bisection(a, b, tol=0.01):
    fa = f(a)
    fb = f(b)
    if fa * fb >= 0:
        print("The bisection method fails.")
        return None
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        fc = f(c)
        if fc == 0 or (b - a) / 2 < tol:
            return c
        if fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc
    return (a + b) / 2

a = 0
b = 1
h_approx = bisection(a, b, tol=0.01)
print(f"The approximate value of h is: {h_approx}")

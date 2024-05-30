import math

a = 0
b = 1
n = 3
def func(x):
    return math.sqrt(x) - math.cos(x)

f_a = func(a)
f_b = func(b)

print("bisection method\n")
for i in range(n):
    p = (a + b) / 2
    print(f"iteration{i + 1}: f(p) = {func(p)}")

    if func(p) * func(a) < 0:
        ...

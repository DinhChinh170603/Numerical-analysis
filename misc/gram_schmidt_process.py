import scipy.integrate as integrate
import math
n = 3
a = 0
b = 3
# phi 0
def w(x):
    return 1 / math.sqrt(1 - x**2)

def phi_0(x):
    return 1

print(f"phi 0: 1")


def phi_k(x):
    if k == 0:
        return 1
    return x - 


# phi 1
B1 = integrate.quad(lambda x: w(x) * phi_0(x), a, b)

print(f"phi 1: x - ")

while True:
    
    pass
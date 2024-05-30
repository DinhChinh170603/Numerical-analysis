import math
import numpy as np
import sympy as sp

float_formatter = "{:.2f}".format
np.set_printoptions(formatter={'float_kind':float_formatter})

degree = 3

x_list = np.array([4.0, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1])
y_list = np.array([102.56, 113.18, 142.05, 167.53, 195.14, 224.87, 299.50, 326.72])

# continuous function
def f(x):
    return 1 / x

def integral_approximation(a, b, degree):
    result, error = 
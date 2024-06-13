from math import pi, e, log, sin, cos, exp

class DerivativeApproximation:
    def approx(self, f, x0, h):
        print("3-point midpoint: ", self.midpoint_rule_3point(f, x0, h))
        print("3-point endpoint: ", self.endpoint_rule_3point(f, x0, h))
        print("5-point midpoint: ", self.midpoint_rule_5point(f, x0, h))
        print("5-point endpoint: ", self.endpoint_rule_5point(f, x0, h))
        print("Second derivative: ", self.snd_derivative(f, x0, h))

    def midpoint_rule_3point(self, f, x0, h):
        d =  (f(x0+h) - f(x0-h)) / (2.0*h)
        return d

    def endpoint_rule_3point(self, f, x0, h):
        d =  (-3*f(x0) + 4*f(x0+h) - f(x0+2*h)) / (2.0*h)
        return d

    def midpoint_rule_5point(self, f, x0, h):
        d = (f(x0-2*h) - 8*f(x0-h) + 8*f(x0+h) - f(x0+2*h)) / (12*h)
        return d

    def endpoint_rule_5point(self, f, x0, h):
        d = (-25*f(x0) + 48*f(x0+h) - 36*f(x0+2*h) + 16*f(x0+3*h) - 3*f(x0+4*h)) / (12.0*h)
        return d
        
    def snd_derivative(self, f, x0, h):
        d = h**(-2) * (f(x0-h) - 2*f(x0) + f(x0+h))
        return d

# Định nghĩa các hàm
def f1(x):
    return exp(2*x) - cos(2*x)

def f2(x):
    return log(x + 2) - (x + 1)**2

def f3(x):
    return x * sin(x) + x**2 * cos(x)

def f4(x):
    return (cos(3*x))**2 - exp(x)

# Các điểm cần tính và bước nhảy h
x_values = [0, 8.0, 1.3, -2.3]
h = 0.1

# Tạo đối tượng DerivativeApproximation
dx = DerivativeApproximation()

# Tính toán và in kết quả
print("Hàm f(x) = e^(2x) - cos(2x) tại x = 0")
dx.approx(f1, 0, h)

print("\nHàm f(x) = ln(x + 2) - (x + 1)^2 tại x = 8.0")
dx.approx(f2, 8.0, h)

print("\nHàm f(x) = x sin x + x^2 cos x tại x = 1.3")
dx.approx(f3, 1.3, h)

print("\nHàm f(x) = (cos 3x)^2 - e^x tại x = -2.3")
dx.approx(f4, -2.3, h)

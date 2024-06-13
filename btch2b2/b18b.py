import numpy as np
import matplotlib.pyplot as plt

def g_b(x):
    return 1 - x**2

def g_b_prime(x):
    return -2 * x

# Vẽ đồ thị để kiểm tra các điểm bất động
x = np.linspace(0, 1, 400)
y = g_b(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$g(x) = 1 - x^2$')
plt.plot(x, x, label='$y = x$', linestyle='--')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.legend()
plt.title('Đồ thị của hàm $g(x) = 1 - x^2$ và $y = x$')
plt.grid(True)
plt.show()

# Tìm các điểm bất động
points = []
for i in range(0, 100):
    p0 = i / 100
    p = p0
    for _ in range(50):
        p = g_b(p)
    if abs(g_b(p) - p) < 1e-4:
        points.append(p)

unique_points = set(np.round(points, 4))
print("Các điểm bất động của hàm g_b trên [0, 1]:", unique_points)

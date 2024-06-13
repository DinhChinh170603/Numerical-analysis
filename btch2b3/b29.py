import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3**(3*x+1) - 7 * 5**(2*x)

# Vẽ đồ thị của hàm f(x)
x = np.linspace(-2, 2, 400)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='$f(x) = 3^{3x+1} - 7 \cdot 5^{2x}$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Đồ thị của hàm $f(x)$')
plt.legend()
plt.grid(True)
plt.show()

# Câu c
# Hàm đạo hàm của f(x)
def f_prime(x):
    return 3**(3*x+1) * 3 * np.log(3) - 7 * 5**(2*x) * 2 * np.log(5)

def newtons_method(f, df, x0, tol=1e-16, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# Giá trị gần đúng ban đầu từ đồ thị
initial_guesses = [-1.5, -0.5, 0.5, 1.5]

# Tìm nghiệm bằng phương pháp Newton
roots = [newtons_method(f, f_prime, x0) for x0 in initial_guesses]
print(f'Nghiệm xấp xỉ của hàm f(x) bằng phương pháp Newton: {roots}')

# Câu d: Tìm nghiệm chính xác
# Biến đổi
# (3x+1)ln(3) = ln(7) + (2x)ln(5)
# 3xln(3) + ln(3) = ln(7) + 2xln(5)
# Đặt x ra ngoài
exact_root = (np.log(7) - np.log(3)) / (3 * np.log(3) - 2 * np.log(5))
print(f'Nghiệm chính xác của hàm f(x) = 0: {exact_root}')

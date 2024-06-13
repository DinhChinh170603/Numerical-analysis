import numpy as np

def euler_method(f, a, b, alpha, N):
    h = (b - a) / N  # Bước nhảy
    t = a
    w = alpha
    
    t_values = np.linspace(a, b, N+1)
    y_values = np.zeros(N+1)
    
    y_values[0] = w
    
    for i in range(1, N + 1):
        w = w + h * f(t, w)  # Tính w_{i+1}
        t = a + i * h  # Tính t_{i+1}
        y_values[i] = w  # Lưu giá trị y
    
    return t_values, y_values

def f_a(t, y):
    return (2 - 2 * t * y) / (t**2 + 1)

def f_b(t, y):
    return y**2 / (1 + t**2)

def f_c(t, y):
    return (y**2 + y) / t

def f_d(t, y):
    return -t * y + 4 * t / y

# Câu a
a_a = 0  # Giá trị biên trái của t
b_a = 1  # Giá trị biên phải của t
alpha_a = 1  # Giá trị ban đầu của y tại t = a
N_a = int((b_a - a_a) / 0.1)  # Số bước chia

t_values_a, y_values_a = euler_method(f_a, a_a, b_a, alpha_a, N_a)
print("Các giá trị t (câu a):", t_values_a)
print("Các giá trị y (câu a):", y_values_a)

# Câu b
a_b = 1  # Giá trị biên trái của t
b_b = 2  # Giá trị biên phải của t
alpha_b = -1 / np.log(2)  # Giá trị ban đầu của y tại t = a
N_b = int((b_b - a_b) / 0.1)  # Số bước chia

t_values_b, y_values_b = euler_method(f_b, a_b, b_b, alpha_b, N_b)
print("Các giá trị t (câu b):", t_values_b)
print("Các giá trị y (câu b):", y_values_b)

# Câu c
a_c = 1  # Giá trị biên trái của t
b_c = 3  # Giá trị biên phải của t
alpha_c = -2  # Giá trị ban đầu của y tại t = a
N_c = int((b_c - a_c) / 0.2)  # Số bước chia

t_values_c, y_values_c = euler_method(f_c, a_c, b_c, alpha_c, N_c)
print("Các giá trị t (câu c):", t_values_c)
print("Các giá trị y (câu c):", y_values_c)

# Câu d
a_d = 0  # Giá trị biên trái của t
b_d = 1  # Giá trị biên phải của t
alpha_d = 1  # Giá trị ban đầu của y tại t = a
N_d = int((b_d - a_d) / 0.1)  # Số bước chia

t_values_d, y_values_d = euler_method(f_d, a_d, b_d, alpha_d, N_d)
print("Các giá trị t (câu d):", t_values_d)
print("Các giá trị y (câu d):", y_values_d)


def exact_solution_a(t):
    return (2 * t + 1) / (t**2 + 1)

def exact_solution_b(t):
    return -1 / np.log(t + 1)

def exact_solution_c(t):
    return 2 * t / (1 - 2 * t)

def exact_solution_d(t):
    return np.sqrt(4 - 3 * np.exp(-t**2))

# Tính sai số
exact_values_a = exact_solution_a(t_values_a)
errors_a = np.abs(y_values_a - exact_values_a)

exact_values_b = exact_solution_b(t_values_b)
errors_b = np.abs(y_values_b - exact_values_b)

exact_values_c = exact_solution_c(t_values_c)
errors_c = np.abs(y_values_c - exact_values_c)

exact_values_d = exact_solution_d(t_values_d)
errors_d = np.abs(y_values_d - exact_values_d)

print("Sai số tại các điểm t (câu a):", errors_a)
print("Sai số tại các điểm t (câu b):", errors_b)
print("Sai số tại các điểm t (câu c):", errors_c)
print("Sai số tại các điểm t (câu d):", errors_d)

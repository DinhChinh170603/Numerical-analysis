import numpy as np

# Phương pháp Heun (Euler Cải tiến)
def heun_method(f, a, b, alpha, N):
    h = (b - a) / N  # Bước nhảy
    t = a
    w = alpha
    
    t_values = np.linspace(a, b, N+1)
    y_values = np.zeros(N+1)
    
    y_values[0] = w
    
    for i in range(1, N + 1):
        t_mid = t + h
        y_pred = w + h * f(t, w)
        w = w + (h / 2) * (f(t, w) + f(t_mid, y_pred))
        t = a + i * h
        y_values[i] = w
    
    return t_values, y_values

# Câu a
def f_a(t, y):
    return t * np.exp(3*t) - 2 * y

a_a = 0  # Giá trị biên trái của t
b_a = 1  # Giá trị biên phải của t
alpha_a = 0  # Giá trị ban đầu của y tại t = a
N_a = int((b_a - a_a) / 0.5)  # Số bước chia

t_values_a, y_values_a = heun_method(f_a, a_a, b_a, alpha_a, N_a)

# Câu b
def f_b(t, y):
    return 1 + (t - y)**2

a_b = 2  # Giá trị biên trái của t
b_b = 3  # Giá trị biên phải của t
alpha_b = 1  # Giá trị ban đầu của y tại t = a
N_b = int((b_b - a_b) / 0.5)  # Số bước chia

t_values_b, y_values_b = heun_method(f_b, a_b, b_b, alpha_b, N_b)

# Câu c
def f_c(t, y):
    return 1 + y / t

a_c = 1  # Giá trị biên trái của t
b_c = 2  # Giá trị biên phải của t
alpha_c = 2  # Giá trị ban đầu của y tại t = a
N_c = int((b_c - a_c) / 0.25)  # Số bước chia

t_values_c, y_values_c = heun_method(f_c, a_c, b_c, alpha_c, N_c)

# Câu d
def f_d(t, y):
    return np.cos(2 * t) + np.sin(3 * t)

a_d = 0  # Giá trị biên trái của t
b_d = 1  # Giá trị biên phải của t
alpha_d = 1  # Giá trị ban đầu của y tại t = a
N_d = int((b_d - a_d) / 0.25)  # Số bước chia

t_values_d, y_values_d = heun_method(f_d, a_d, b_d, alpha_d, N_d)

# In kết quả
print("Các giá trị t (câu a):", t_values_a)
print("Các giá trị y (câu a):", y_values_a)
print("\n")
print("Các giá trị t (câu b):", t_values_b)
print("Các giá trị y (câu b):", y_values_b)
print("\n")
print("Các giá trị t (câu c):", t_values_c)
print("Các giá trị y (câu c):", y_values_c)
print("\n")
print("Các giá trị t (câu d):", t_values_d)
print("Các giá trị y (câu d):", y_values_d)
print("\n")

# Tính sai số thực tế

# Câu a
def exact_solution_a(t):
    return (1/5) * t * np.exp(3*t) - (1/25) * np.exp(3*t) + (1/25) * np.exp(-2*t)

exact_values_a = exact_solution_a(t_values_a)
errors_a = np.abs(y_values_a - exact_values_a)

# Câu b
def exact_solution_b(t):
    return t + 1 / (1 - t)

exact_values_b = exact_solution_b(t_values_b)
errors_b = np.abs(y_values_b - exact_values_b)

# Câu c
def exact_solution_c(t):
    return t * np.log(t) + 2*t

exact_values_c = exact_solution_c(t_values_c)
errors_c = np.abs(y_values_c - exact_values_c)

# Câu d
def exact_solution_d(t):
    return (1/2) * np.sin(2*t) - (1/3) * np.cos(3*t) + (4/3)

exact_values_d = exact_solution_d(t_values_d)
errors_d = np.abs(y_values_d - exact_values_d)

print("Sai số tại các điểm t (câu a):", errors_a)
print("Sai số tại các điểm t (câu b):", errors_b)
print("Sai số tại các điểm t (câu c):", errors_c)
print("Sai số tại các điểm t (câu d):", errors_d)

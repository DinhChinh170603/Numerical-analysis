import numpy as np

# Phương pháp Runge-Kutta bậc 4 (RK4)
def rk4(f, t0, y0, t_end, h):
    """
    Hàm thực hiện phương pháp Runge-Kutta bậc 4 để giải phương trình vi phân y' = f(t, y).
    
    :param f: Hàm f(t, y) đại diện cho phương trình vi phân.
    :param t0: Giá trị ban đầu của biến t.
    :param y0: Giá trị ban đầu của hàm y.
    :param t_end: Giá trị cuối cùng của t.
    :param h: Bước nhảy (khoảng cách giữa các giá trị t liên tiếp).
    :return: Mảng các giá trị t và y tương ứng.
    """
    t_values = np.arange(t0, t_end + h, h)  # Tạo mảng các giá trị t từ t0 đến t_end với bước nhảy h
    y_values = np.zeros((len(t_values), len([y0])))  # Khởi tạo mảng các giá trị y với độ dài tương ứng
    y_values[0] = y0  # Gán giá trị ban đầu cho y
    
    for i in range(1, len(t_values)):  # Lặp qua tất cả các giá trị t
        t = t_values[i-1]  # Lấy giá trị t hiện tại
        y = y_values[i-1]  # Lấy giá trị y hiện tại
        
        # Tính các hệ số k1, k2, k3, k4
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        
        # Tính giá trị y tiếp theo
        y_values[i] = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return t_values, y_values  # Trả về mảng các giá trị t và y

# Câu a
def f_a(t, y):
    return t * np.exp(3*t) - 2 * y  # Hàm f(t, y) cho câu a

t0_a, y0_a = 0, 0  # Giá trị ban đầu của t và y
t_end_a, h_a = 1, 0.5  # Giá trị cuối cùng của t và bước nhảy

t_values_a, y_values_a = rk4(f_a, t0_a, y0_a, t_end_a, h_a)  # Áp dụng phương pháp RK4 cho câu a

# Câu b
def f_b(t, y):
    return 1 + (t - y)**2  # Hàm f(t, y) cho câu b

t0_b, y0_b = 2, 1  # Giá trị ban đầu của t và y
t_end_b, h_b = 3, 0.5  # Giá trị cuối cùng của t và bước nhảy

t_values_b, y_values_b = rk4(f_b, t0_b, y0_b, t_end_b, h_b)  # Áp dụng phương pháp RK4 cho câu b

# Câu c
def f_c(t, y):
    return 1 + y / t  # Hàm f(t, y) cho câu c

t0_c, y0_c = 1, 2  # Giá trị ban đầu của t và y
t_end_c, h_c = 2, 0.25  # Giá trị cuối cùng của t và bước nhảy

t_values_c, y_values_c = rk4(f_c, t0_c, y0_c, t_end_c, h_c)  # Áp dụng phương pháp RK4 cho câu c

# Câu d
def f_d(t, y):
    return np.cos(2*t) + np.sin(3*t)  # Hàm f(t, y) cho câu d

t0_d, y0_d = 0, 1  # Giá trị ban đầu của t và y
t_end_d, h_d = 1, 0.25  # Giá trị cuối cùng của t và bước nhảy

t_values_d, y_values_d = rk4(f_d, t0_d, y0_d, t_end_d, h_d)  # Áp dụng phương pháp RK4 cho câu d

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
    return (1/5) * t * np.exp(3*t) - (1/25) * np.exp(3*t) + (1/25) * np.exp(-2*t)  # Hàm giải chính xác cho câu a

exact_values_a = exact_solution_a(t_values_a)
errors_a = np.abs(y_values_a - exact_values_a)  # Tính sai số cho câu a

# Câu b
def exact_solution_b(t):
    return t + 1 / (1 - t)  # Hàm giải chính xác cho câu b

exact_values_b = exact_solution_b(t_values_b)
errors_b = np.abs(y_values_b - exact_values_b)  # Tính sai số cho câu b

# Câu c
def exact_solution_c(t):
    return t * np.log(t) + 2*t  # Hàm giải chính xác cho câu c

exact_values_c = exact_solution_c(t_values_c)
errors_c = np.abs(y_values_c - exact_values_c)  # Tính sai số cho câu c

# Câu d
def exact_solution_d(t):
    return (1/2) * np.sin(2*t) - (1/3) * np.cos(3*t) + (4/3)  # Hàm giải chính xác cho câu d

exact_values_d = exact_solution_d(t_values_d)
errors_d = np.abs(y_values_d - exact_values_d)  # Tính sai số cho câu d

print("Sai số tại các điểm t (câu a):", errors_a)
print("Sai số tại các điểm t (câu b):", errors_b)
print("Sai số tại các điểm t (câu c):", errors_c)
print("Sai số tại các điểm t (câu d):", errors_d)

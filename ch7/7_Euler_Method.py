import numpy as np

def euler_method(f, a, b, alpha, N):
    """
    Phương pháp Euler để giải bài toán giá trị ban đầu y' = f(t, y), y(a) = alpha
    :param f: Hàm f(t, y)
    :param a: Giá trị biên trái của t
    :param b: Giá trị biên phải của t
    :param alpha: Giá trị ban đầu của y tại t = a
    :param N: Số bước chia
    :return: Các giá trị t và y
    """
    h = (b - a) / N  # Bước nhảy
    t = a
    w = alpha
    
    t_values = np.linspace(a, b, N+1)
    y_values = np.zeros(N+1)
    
    y_values[0] = w
    
    # Step 2: Vòng lặp cho các bước từ 1 đến N
    for i in range(1, N + 1):
        w = w + h * f(t, w)  # Tính w_{i+1}
        t = a + i * h  # Tính t_{i+1}
        y_values[i] = w  # Lưu giá trị y
    
    return t_values, y_values

# Ví dụ áp dụng phương pháp Euler
def f(t, y):
    return t - y**2

a = 0  # Giá trị biên trái của t
b = 2  # Giá trị biên phải của t
alpha = 0.5  # Giá trị ban đầu của y tại t = a
N = 10  # Số bước chia

t_values, y_values = euler_method(f, a, b, alpha, N)

print("Các giá trị t:", t_values)
print("Các giá trị y:", y_values)

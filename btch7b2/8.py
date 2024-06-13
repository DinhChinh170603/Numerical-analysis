import numpy as np

def taylor_order4(f, df_dt, df_dy, d2f_dt2, d2f_dtdy, d2f_dy2, d3f_dt3, d3f_dt2dy, d3f_dtdy2, d3f_dy3, d4f_dt4, d4f_dt3dy, d4f_dt2dy2, d4f_dtdy3, d4f_dy4, a, b, alpha, N):
    """
    Phương pháp Taylor bậc 4 để giải bài toán giá trị ban đầu y' = f(t, y), y(a) = alpha
    :param f: Hàm f(t, y)
    :param df_dt: Đạo hàm bậc 1 của f theo t
    :param df_dy: Đạo hàm bậc 1 của f theo y
    :param d2f_dt2: Đạo hàm bậc 2 của f theo t
    :param d2f_dtdy: Đạo hàm bậc 2 của f theo t và y
    :param d2f_dy2: Đạo hàm bậc 2 của f theo y
    :param d3f_dt3: Đạo hàm bậc 3 của f theo t
    :param d3f_dt2dy: Đạo hàm bậc 3 của f theo t và y
    :param d3f_dtdy2: Đạo hàm bậc 3 của f theo t và y^2
    :param d3f_dy3: Đạo hàm bậc 3 của f theo y
    :param d4f_dt4: Đạo hàm bậc 4 của f theo t
    :param d4f_dt3dy: Đạo hàm bậc 4 của f theo t và y
    :param d4f_dt2dy2: Đạo hàm bậc 4 của f theo t và y^2
    :param d4f_dtdy3: Đạo hàm bậc 4 của f theo t và y^3
    :param d4f_dy4: Đạo hàm bậc 4 của f theo y
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
    
    for i in range(1, N + 1):
        y_prime = f(t, w)
        y_double_prime = df_dt(t, w) + df_dy(t, w) * y_prime
        y_triple_prime = d2f_dt2(t, w) + 2 * d2f_dtdy(t, w) * y_prime + d2f_dy2(t, w) * (y_prime ** 2) + df_dy(t, w) * y_double_prime
        y_quad_prime = d3f_dt3(t, w) + 3 * d3f_dt2dy(t, w) * y_prime + 3 * d3f_dtdy2(t, w) * (y_prime ** 2) + d3f_dy3(t, w) * (y_prime ** 3) + 3 * d2f_dtdy(t, w) * y_double_prime + 3 * d2f_dy2(t, w) * y_prime * y_double_prime + df_dy(t, w) * y_triple_prime
        
        w = w + h * y_prime + (h ** 2 / 2) * y_double_prime + (h ** 3 / 6) * y_triple_prime + (h ** 4 / 24) * y_quad_prime
        t = a + i * h
        y_values[i] = w
    
    return t_values, y_values

# Định nghĩa phương trình vi phân và các đạo hàm
def f(t, y):
    return (2 - 2 * t * y) / (t**2 + 1)

def df_dt(t, y):
    return -4 * t / (t**2 + 1)**2

def df_dy(t, y):
    return -2 * t / (t**2 + 1)

def d2f_dt2(t, y):
    return 8 * t**2 / (t**2 + 1)**3

def d2f_dtdy(t, y):
    return 4 * t**2 / (t**2 + 1)**2

def d2f_dy2(t, y):
    return 0

def d3f_dt3(t, y):
    return -48 * t**3 / (t**2 + 1)**4

def d3f_dt2dy(t, y):
    return -8 * t / (t**2 + 1)**3

def d3f_dtdy2(t, y):
    return 0

def d3f_dy3(t, y):
    return 0

def d4f_dt4(t, y):
    return 384 * t**4 / (t**2 + 1)**5

def d4f_dt3dy(t, y):
    return 48 * t**2 / (t**2 + 1)**4

def d4f_dt2dy2(t, y):
    return 0

def d4f_dtdy3(t, y):
    return 0

def d4f_dy4(t, y):
    return 0

a = 0  # Giá trị biên trái của t
b = 1  # Giá trị biên phải của t
alpha = 1  # Giá trị ban đầu của y tại t = a
N = 10  # Số bước chia

t_values, y_values = taylor_order4(f, df_dt, df_dy, d2f_dt2, d2f_dtdy, d2f_dy2, d3f_dt3, d3f_dt2dy, d3f_dtdy2, d3f_dy3, d4f_dt4, d4f_dt3dy, d4f_dt2dy2, d4f_dtdy3, d4f_dy4, a, b, alpha, N)

print("Các giá trị t:", t_values)
print("Các giá trị y:", y_values)

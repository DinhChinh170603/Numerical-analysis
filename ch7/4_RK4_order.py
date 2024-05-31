import numpy as np
import math

# Hệ phương trình vi phân
def df(x, y: np.array):
    # Res0-1 là các phương trình vi phân của hệ.
    res = np.ndarray(2)
    # Định nghĩa phương trình thứ nhất
    res[0] = 1/9 * y[0] - 2/3 * y[1] + 1 / 9 * x ** 2 + 2/3
    # Định nghĩa phương trình thứ hai
    res[1] = y[1] + 3 * x - 4
    return res

# Hàm tính giá trị thực tế
def _actual(x):
    # Hàm này tính giá trị thực tế của hệ phương trình tại điểm x
    res = np.ndarray(2)
    # Tính giá trị thực tế của phương trình thứ nhất
    res[0] = -3 * math.e ** x + x ** 2
    # Tính giá trị thực tế của phương trình thứ hai
    res[1] = 4 * math.e ** x - 3 * x + 1
    return res

# Hàm phương pháp Runge-Kutta bậc 4
def RK4(x, y: np.array, h):
    # Hàm này thực hiện phương pháp Runge-Kutta bậc 4 để tính giá trị mới của y tại bước nhảy h
    # Tính k1
    k1 = df(x, y)
    # Tính k2
    k2 = df(x + 0.5 * h, y + 0.5 * h * k1)
    # Tính k3
    k3 = df(x + 0.5 * h, y + 0.5 * h * k2)
    # Tính k4
    k4 = df(x + h, y + h * k3)
    # Tính y1 dựa trên k1, k2, k3, k4
    y1 = y + h/6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return y1

def main():
    # Điều kiện ban đầu
    t = 0
    y = np.array([-3, 5])
    h = 0.2  # Tùy chỉnh bước nhảy
    iteration = 10

    print('Phương pháp Runge-Kutta bậc 4:')
    for i in range(iteration):
        print(f'Điểm mốc thứ {i + 1}')
        # Tính y1 bằng phương pháp Runge-Kutta bậc 4
        y1 = RK4(t, y, h)
        # In kết quả
        print(f'u1 = {round(y1[0], 10)}, u2 = {round(y1[1], 10)}')
        # Cập nhật giá trị y và t
        y = y1
        t = round(i * h + h, 3)
    
    print(f'\nGiá trị thực tế tại x=2: {_actual(2)}')
    print(f'Sai số: {y -  _actual(2)}')

main()

import numpy as np
import math

# Giá trị ban đầu và bước nhảy
x0 = 1
y0 = -4
h = 0.01

# Hàm gốc cần tính đạo hàm
def func(x):
    return 1 + x ** 2

# Hàm tính đạo hàm sử dụng công thức đối xứng để cải thiện độ chính xác
def df(func, x, order=1):
    h = 1e-5  # Bước nhảy nhỏ để tính đạo hàm

    if order > 1:
        # Đạo hàm cấp cao hơn bằng cách gọi đệ quy
        return (df(func, x + h, order - 1) - df(func, x - h, order - 1)) / (2 * h)
    
    # Đạo hàm cấp 1
    return func(x)

# Hàm tính chuỗi Taylor
def taylor_series(x: float, y, h, iteration, order=1):
    if order == 1:
        print("Phương pháp Newton.")
    else:
        print("Phương pháp chuỗi Taylor.")

    for i in range(iteration):
        print(f'Số lần lặp {i}')

        temp = y  # Khởi tạo giá trị tạm thời của y
        # Tính chuỗi Taylor bậc cao
        for j in range(1, order + 1):
            # Cộng thêm từng hạng tử của chuỗi Taylor
            temp += h**j / math.factorial(j) * df(func, x, j)

        print(f'x = {x}')
        print(f'y = {y}')
        y = temp  # Cập nhật giá trị của y
        x = x + h  # Cập nhật giá trị của x

# Ví dụ sử dụng hàm tính chuỗi Taylor
taylor_series(x0, y0, h, 4, 1)

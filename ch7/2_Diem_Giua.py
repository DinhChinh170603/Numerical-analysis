import math

# Bước nhảy và giá trị ban đầu
h = 0.1
x0 = 0
y0 = 1 / 3

# Hàm gốc cần giải phương trình vi phân
def func(x, y):
    return -5 * y + 5 * x ** 2 + 2 * x # y' = -5y + 5x^2 + 2x
# Hàm này biểu diễn phương trình vi phân cần giải.

# Hàm thực hiện phương pháp điểm giữa
def mid_point(x, y, h, iteration):
    # x: Giá trị ban đầu của x.
    # y: Giá trị ban đầu của y.
    # h: Bước nhảy.
    # iteration: Số lần lặp.
    print("Phương pháp điểm giữa:")

    for i in range(iteration):
        print(f'lần lặp {i + 1}')

        # Tính giá trị trung gian
        x_mid = x + h * 0.5
        y_mid = y + h * 0.5 * func(x, y)
        
        # Tính giá trị tại điểm cuối
        y = y + h * func(x_mid, y_mid)

        print(f'x = {x}')
        print(f'y = {y}')

        # Cập nhật giá trị của x
        x = x + h

# Ví dụ sử dụng phương pháp điểm giữa
mid_point(x0, y0, h, 10)

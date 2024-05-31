import math

# Bước nhảy và giá trị ban đầu
h = 0.1
x = 0
y = 1 / 3

# Hàm gốc cần giải phương trình vi phân
def func(x, y):
    return -5 * y + 5 * x ** 2 + 2 * x

# Hàm tiên đoán (predictor)
def predictor(x, y, h):
    return y + h * func(x, y) # Hàm này tính giá trị tiên đoán y_pred

# Hàm hiệu chỉnh (corrector)
def corrector(x, y, h, pred):
    return y + h / 2 * (func(x, y) + func(x, pred)) # Hàm này tính giá trị hiệu chỉnh y_corr

# Hàm tính giá trị thực tế của hàm (dùng để so sánh lỗi)
def actual(x):
    return x ** 2 + 1 / 3 * math.e ** (-5 * x) #Hàm này tính giá trị thực tế của hàm tại điểm x

# Hàm thực hiện phương pháp tiên đoán-hiệu chỉnh Heun
def mid_point(x, y, h, iteration):
    print("Phương pháp tiên đoán-hiệu chỉnh Heun:")

    for i in range(iteration):
        print(f'lần lặp {i + 1}')

        # Bước tiên đoán
        _pred = predictor(x, y, h)
        print(f'giá trị tiên đoán: {_pred}')

        # Bước hiệu chỉnh
        _correct = corrector(x, y, h, _pred)
        print(f'giá trị hiệu chỉnh: {_correct}')

        # Tính và in lỗi
        print(f'giá trị thực tế: y = {actual(x + h)}')
        print(f'sai số: {abs(y - actual(x))}')
        
        # Cập nhật giá trị y và x
        y = _correct
        x = x + h

# Ví dụ sử dụng phương pháp tiên đoán-hiệu chỉnh Heun
mid_point(x, y, h, 10)

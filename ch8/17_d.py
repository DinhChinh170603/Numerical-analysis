import math

h = 0.1
x = 0
y = 1 / 3

x_y_pair = [(0, round(1/3, 6))]
error_save = []

def f(x, y):
    return -5 * y + 5 * x ** 2 + 2 * x

def predictor(x, y, h):
    return y + h * f(x, y)

def corrector(x, y, h, pred):
    return y + h / 2 * (f(x, y) + f(x, pred))

def actual(x):
    return x ** 2 + 1 / 3 * math.e ** (-5 * x)

def cal_error(y, y_pred):
    return abs(y - y_pred)

# nửa đầu bài 17b sử dụng kết quả bài 3
for i in range(1, 11):
    print(f'\nvòng lặp {i}: ')
    print(f'x: {x}, y: {y}')

    _pred = predictor(x, y, h)
    print(f'predictor: {_pred}')

    _correct = corrector(x, y, h, _pred)
    print(f'corrector: {_correct}')
    # print(f'kết quả thực tế: {actual(x + h)}')

    y = round(_correct, 6)
    x = round(h * i, 6)

    x_y_pair.append((x, y))

    # print(f'error: {cal_error(y, actual(x))}')


# nửa sau sử dụng nội suy tuyến tính
def linear_interpolation(p1, p2, x):
    # pass
    x0, y0 = p1
    x1, y1 = p2

    L0 = (x - x1) / (x0 - x1)
    L1 = (x - x0) / (x1 - x0)

    return y0 * L0 + y1 * L1 


print(f'\nNội suy tuyên tính')


print(f'y(5.4) = {round(linear_interpolation(x_y_pair[5],x_y_pair[6], 0.54 ), 6)}')  
print(f'kết quả thực tế: y(0.54) = {round(actual(0.54), 6)}')
print(f'sai số: {round(linear_interpolation(x_y_pair[5],x_y_pair[6], 0.54 ) - actual(0.54), 6)}')

print(f'\ny(9.4) = {round(linear_interpolation(x_y_pair[9],x_y_pair[10], 0.94 ), 6)}')
print(f'kết quả thực tế: y(0.94) = {round(actual(0.94), 6)}')
print(f'sai số: {round(linear_interpolation(x_y_pair[9],x_y_pair[10], 0.94 ) - actual(0.94), 6)}')






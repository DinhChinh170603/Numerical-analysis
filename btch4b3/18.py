import numpy as np

def divided_differences(points: np.ndarray):
    """ Tính bảng sai phân chia cho Newton's polynomial interpolation. """
    n = len(points)
    f = np.zeros((n, n))  # Khởi tạo bảng sai phân
    
    # Điền cột đầu tiên với giá trị y tại các điểm
    for i in range(n):
        f[i][0] = points[i][1]
    
    # Tính các sai phân chia
    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i + 1][j - 1] - f[i][j - 1]) / (points[i + j][0] - points[i][0])
    
    return f[0]  # Trả về các hệ số sai phân chia cho đa thức nội suy

def newton_polynomial(points: np.ndarray, x: float):
    """ Tính giá trị nội suy tại x bằng đa thức Newton. """
    # tính giá trị nội suy tại một điểm dựa trên bảng sai phân chia.
    coefficients = divided_differences(points)
    n = len(points)
    result = coefficients[0]
    product_term = 1
    for i in range(1, n):
        product_term *= (x - points[i - 1][0])
        result += coefficients[i] * product_term
    return result

# Dữ liệu dân số theo năm từ 1950 đến 2000
points = np.array([
    [1950, 151325798],
    [1960, 179323175],
    [1970, 203211926],
    [1980, 226545805],
    [1990, 248709873],
    [2000, 281421906]
], dtype=float)

# Tính giá trị nội suy cho các năm 1940, 1975, và 2020
years = [1940, 1975, 2020]
for year in years:
    population = newton_polynomial(points, year)
    print(f"Dân số ước tính vào năm {year} là {population:.0f}")

# So sánh với giá trị thực tế của năm 1940
actual_population_1940 = 132165000
estimated_population_1940 = newton_polynomial(points, 1940)
print(f"Giá trị thực tế của dân số năm 1940: {actual_population_1940}")
print(f"Giá trị ước tính của dân số năm 1940: {estimated_population_1940:.0f}")

# Đánh giá độ chính xác của giá trị ước tính cho năm 1975 và 2020 so với giá trị ước tính năm 1940

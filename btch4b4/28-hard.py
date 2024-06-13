import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Dữ liệu dân số từ năm 1950 đến 2000
years = np.array([1950, 1960, 1970, 1980, 1990, 2000])  # Năm
population = np.array([151325798, 179323175, 203211926, 226545805, 248709873, 281421906])  # Dân số

# Xây dựng spline bậc ba tự nhiên
spline = CubicSpline(years, population, bc_type='natural')  # Tạo spline bậc ba với điều kiện biên tự nhiên

# Xấp xỉ dân số vào các năm 1940, 1975 và 2020
years_to_approximate = [1940, 1975, 2020]  # Năm cần nội suy
approximations = spline(years_to_approximate)  # Tính giá trị nội suy

print(f"Dân số ước lượng vào năm 1940: {approximations[0]:.0f}")
print(f"Dân số ước lượng vào năm 1975: {approximations[1]:.0f}")
print(f"Dân số ước lượng vào năm 2020: {approximations[2]:.0f}")

# Dân số thực tế vào năm 1940 là khoảng 132,165,000
actual_1940_population = 132165000
print(f"Dân số thực tế vào năm 1940: {actual_1940_population}")

# Đánh giá độ chính xác của các số liệu 1975 và 2020
errors = {
    1940: approximations[0] - actual_1940_population,
    1975: approximations[1] - actual_1940_population,  # Không có số liệu thực tế, so sánh với 1940 để có một ước lượng
    2020: approximations[2] - actual_1940_population   # Không có số liệu thực tế, so sánh với 1940 để có một ước lượng
}

print(f"Sai số ước lượng vào năm 1940: {errors[1940]:.0f}")
print(f"Sai số ước lượng vào năm 1975: {errors[1975]:.0f}")
print(f"Sai số ước lượng vào năm 2020: {errors[2020]:.0f}")

# Vẽ đồ thị spline
plt.figure(figsize=(10, 6))  # Kích thước đồ thị
plt.plot(years, population, 'o', label='Dữ liệu thực tế')  # Vẽ các điểm dữ liệu thực tế
plt.plot(years_to_approximate, approximations, 'x', label='Dữ liệu nội suy')  # Vẽ các điểm nội suy
plt.plot(np.arange(1940, 2021, 1), spline(np.arange(1940, 2021, 1)), label='Spline bậc ba tự nhiên')  # Vẽ đường spline
plt.xlabel('Năm')  # Nhãn trục x
plt.ylabel('Dân số')  # Nhãn trục y
plt.legend()  # Hiển thị chú thích
plt.title('Nội suy spline bậc ba tự nhiên cho dân số Hoa Kỳ')  # Tiêu đề đồ thị
plt.grid(True)  # Hiển thị lưới
plt.show()  # Hiển thị đồ thị

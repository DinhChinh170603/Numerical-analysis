import numpy as np

# Khởi tạo các điểm dữ liệu
x = np.array([0.0, 0.4, 0.7])
f = np.zeros((3, 3))  # Tạo bảng sai phân chia có kích thước 3x3

# Gán các giá trị đã cho
f[0][0] = np.nan  # f[x0], giá trị chưa biết
f[1][0] = np.nan  # f[x1], giá trị chưa biết
f[2][0] = 6  # f[x2] đã biết là 6
f[0][1] = np.nan  # f[x0, x1], giá trị chưa biết
f[1][1] = 10  # f[x1, x2] đã biết là 10
f[0][2] = 50 / 7  # f[x0, x1, x2] đã biết là 50/7

# Tính các giá trị còn thiếu
# Tính f[x1]
f[1][0] = f[2][0] - f[1][1] * (x[2] - x[1])  # Sử dụng công thức sai phân chia

# Tính f[x0, x1]
f[0][1] = f[1][1] - f[0][2] * (x[1] - x[0])  # Sử dụng công thức sai phân chia

# Tính f[x0]
f[0][0] = f[1][0] - f[0][1] * (x[1] - x[0])  # Sử dụng công thức sai phân chia

# In ra kết quả
print(f"f[x0] = {f[0][0]}") 
print(f"f[x1] = {f[1][0]}")  
print(f"f[x2] = {f[2][0]}")  
print(f"f[x0, x1] = {f[0][1]}") 
print(f"f[x1, x2] = {f[1][1]}") 
print(f"f[x0, x1, x2] = {f[0][2]}")  

import numpy as np

# Dữ liệu được cung cấp trong bài toán
F = np.array([2, 4, 6])  # Các giá trị lực F(l)
l = np.array([7.0, 9.4, 12.3])  # Các giá trị chiều dài l
E = 5.3  # Chiều dài tự nhiên của lò xo

# Tính x = l - E
x = l - E

# Thiết lập ma trận A và vector b để sử dụng phương pháp bình phương tối thiểu
A = np.vstack([x, np.ones(len(x))]).T
b = F

# Sử dụng hàm lstsq của numpy để tìm giải pháp bình phương tối thiểu
k, _ = np.linalg.lstsq(A, b, rcond=None)[0]

print(f"Giá trị tối ưu của k (hằng số lò xo) là: {k:.4f}")

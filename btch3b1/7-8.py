import numpy as np

def gaussian_elimination(A):
    n = len(A)
    
    # Phần khử Gauss
    for i in range(n):
        # Tìm phần tử chính của cột hiện tại
        max_el = abs(A[i][i])
        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > max_el:
                max_el = abs(A[k][i])
                max_row = k
        
        # Đổi chỗ hàng hiện tại với hàng có phần tử chính lớn nhất
        A[[i, max_row]] = A[[max_row, i]]
        
        # Kiểm tra có tồn tại giải hay không
        if A[i][i] == 0:
            raise ValueError("No unique solution exists")
        
        # Khử các hàng dưới
        for k in range(i+1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Quy hoàn ngược
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = A[i][n] / A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    
    return x

# Ví dụ sử dụng
if __name__ == "__main__":
    A_a = np.array([[1/4, 1/5, 1/6, 9],
                [1/3, 1/4, 1/5, 8],
                [1/2, 1, 2, 8]], dtype=float)
    solution = gaussian_elimination(A_a)
    print("Nghiệm của hệ phương trình là:", solution)

# A_b = np.array([[3.333, 15920, -10.333, 15913],
#                 [2.222, 16.71, 9.612, 28.544],
#                 [1.5611, 5.1791, 1.6852, 8.4254]], dtype=float)

# A_c = np.array([[1, 1/2, 1/3, 1/4, 1/6],
#                 [1/2, 1/3, 1/4, 1/5, 1/7],
#                 [1/3, 1/4, 1/5, 1/6, 1/8],
#                 [1/4, 1/5, 1/6, 1/7, 1/9]], dtype=float)

# A_d = np.array([[2, 1, -1, -1, -3, 7],
#                 [1, 2, -1, -1, -1, 2],
#                 [-2, 0, -1, 1, -1, -5],
#                 [3, 1, -2, 0, 5, 6],
#                 [1, -1, -1, -1, 1, 3]], dtype=float)

########## 8
# A_a = np.array([[1/2, 1/4, -1/8, 0],
#                 [1/3, -1/6, 1/9, 1],
#                 [1/7, 1/5, 1/10, 2]], dtype=float)

# A_b = np.array([[2.71, 1, 1032, 12],
#                 [4.12, -1, 500, 11.49],
#                 [3.33, 2, -200, 41]], dtype=float)

# A_c = np.array([[math.pi, math.sqrt(2), -1, 1, 0],
#                 [math.e, -1, 1, 2, 1],
#                 [1, 1, -math.sqrt(3), 1, 2],
#                 [-1, -1, 1, -math.sqrt(5), 3]], dtype=float)

# A_d = np.array([[1, 1, -1, 1, -1, 2],
#                 [2, 2, 1, -1, 1, 4],
#                 [3, 1, -3, -2, 3, 8],
#                 [4, 1, -2, 4, -5, 16],
#                 [16, -1, -1, -1, -1, 32]], dtype=float)

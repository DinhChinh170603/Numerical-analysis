import numpy as np

def gaussian_elimination_gauss_jordan(A):
    n = len(A)
    
    # Khử Gauss để giảm hệ phương trình thành dạng tam giác
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
        
        # Kiểm tra nếu không có nghiệm duy nhất
        if A[i][i] == 0:
            raise ValueError("No unique solution exists")
        
        # Khử các phần tử dưới phần tử chính
        for k in range(i+1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Khử Gauss-Jordan để giảm hệ phương trình thành dạng bậc thang hàng giảm dần
    for i in range(n-1, -1, -1):
        for k in range(i-1, -1, -1):
            c = -A[k][i] / A[i][i]
            for j in range(n, i-1, -1):
                A[k][j] += c * A[i][j]
    
    # Chuẩn hóa các hàng
    for i in range(n):
        A[i, n] = A[i, n] / A[i, i]
        A[i, i] = 1
    
    return A[:, n]

# Hệ phương trình a
A_a = np.array([[1/2, 1/4, -1/8, 0],
                [1/3, -1/6, 1/9, 1],
                [1/7, 1/5, 1/10, 2]], dtype=float)

# Hệ phương trình b
A_b = np.array([[3.333, 15920, -10.333, 15913],
                [2.222, 16.71, 9.612, 28.544],
                [1.5611, 5.1791, 1.6852, 8.4254]], dtype=float)

# Hệ phương trình c
A_c = np.array([[np.pi, np.sqrt(2), -1, 1, 0],
                [np.e, -1, 1, 2, 1],
                [1, 1, -np.sqrt(3), 1, 2],
                [-1, -1, 1, -np.sqrt(5), 3]], dtype=float)

# Hệ phương trình d
A_d = np.array([[1, 1, -1, 1, -1, 2],
                [2, 2, 1, -1, 1, 4],
                [3, 1, -3, -2, 3, 8],
                [4, 1, -2, 4, -5, 16],
                [16, -1, -1, -1, -1, 32]], dtype=float)

# Giải các hệ phương trình
solution_a = gaussian_elimination_gauss_jordan(A_a)
print("Nghiệm của hệ phương trình a:", solution_a)

solution_b = gaussian_elimination_gauss_jordan(A_b)
print("Nghiệm của hệ phương trình b:", solution_b)

solution_c = gaussian_elimination_gauss_jordan(A_c)
print("Nghiệm của hệ phương trình c:", solution_c)

solution_d = gaussian_elimination_gauss_jordan(A_d)
print("Nghiệm của hệ phương trình d:", solution_d)

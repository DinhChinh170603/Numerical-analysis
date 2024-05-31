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
    A = np.array([[2, 1, -1, 8],
                  [-3, -1, 2, -11],
                  [-2, 1, 2, -3]], dtype=float)
    solution = gaussian_elimination(A)
    print("Nghiệm của hệ phương trình là:", solution)

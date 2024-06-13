import numpy as np

def gaussian_elimination_gauss_jordan(A):
    n = len(A)
    
    # Khử Gauss để giảm hệ phương trình thành dạng tam giác
    for i in range(n):
        # Tìm phần tử chính của cột hiện tại
        max_el = abs(A[i][i]) #Tìm phần tử chính:
        max_row = i
        for k in range(i+1, n): #Lặp qua các hàng để tìm phần tử lớn nhất:
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
    for i in range(n-1, -1, -1): #Khử các phần tử phía trên phần tử chính:
        for k in range(i-1, -1, -1): #Lặp qua các hàng để khử các phần tử phía trên:
            c = -A[k][i] / A[i][i]
            for j in range(n, i-1, -1):
                A[k][j] += c * A[i][j]
    
    # Chuẩn hóa các hàng
    for i in range(n):
        A[i, n] = A[i, n] / A[i, i]  # Chia toàn bộ hàng cho phần tử chính để phần tử chính bằng 1
        A[i, i] = 1  # Đặt phần tử chính bằng 1
    
    return A[:, n]  # Trả về nghiệm của hệ phương trình

# Ví dụ sử dụng cho bài tập 3
A1 = np.array([[4, -1, 1, 8],
               [2, 5, 2, 3],
               [1, 2, 4, 11]], dtype=float)  # Hệ phương trình 3a

A2 = np.array([[4, 1, 2, 9],
               [2, 4, -1, -5],
               [1, 1, -3, -9]], dtype=float)  # Hệ phương trình 3b

solution1 = gaussian_elimination_gauss_jordan(A1)
print("Nghiệm của hệ phương trình 3a:", solution1)

solution2 = gaussian_elimination_gauss_jordan(A2)
print("Nghiệm của hệ phương trình 3b:", solution2)

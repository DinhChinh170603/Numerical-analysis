import numpy as np

def isPositiveDefinite(A: np.ndarray):
    """ Kiểm tra ma trận A có là ma trận xác định dương không dựa trên các trị riêng. """
    return np.all(np.linalg.eigvals(A) > 0)

def choleskyMethod(A: np.ndarray) -> np.ndarray:
    """ Thực hiện phân rã Cholesky cho ma trận xác định dương A. """
    if not isPositiveDefinite(A):
        raise Exception("A is not positive definite matrix!")

    n = len(A)
    L = np.zeros((n, n))  # Khởi tạo ma trận L là ma trận tam giác dưới

    # Duyệt qua mỗi hàng i
    for i in range(n):
        # Tính L[i][i], đây là căn bậc hai của A[i][i] trừ đi tổng bình phương các phần tử của L[i] từ đầu đến i-1
        sumSqr = np.sum(L[i, :i]**2)
        L[i, i] = np.sqrt(A[i, i] - sumSqr)

        # Duyệt qua mỗi cột j từ i đến n để cập nhật các phần tử L[j][i]
        for j in range(i + 1, n):
            # Tính tổng sản phẩm của các phần tử tương ứng từ L[i] và L[j] cho đến i-1
            sumRow = np.dot(L[i, :i], L[j, :i])
            L[j, i] = (A[j, i] - sumRow) / L[i, i]

    return L

# Ví dụ sử dụng
if __name__ == "__main__":
    A = np.array([
        [9, -3, 3],
        [-3, 10, 1],
        [3, 1, 5]])
    print("Ma trận L:")
    print(choleskyMethod(A))

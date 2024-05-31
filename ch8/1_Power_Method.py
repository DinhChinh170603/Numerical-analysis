import numpy as np

def power_method(A, x, TOL, N):
    n = len(A)
    k = 1

    # Step 2: Tìm chỉ số của phần tử có giá trị tuyệt đối lớn nhất trong x
    p = np.argmax(np.abs(x))

    # Step 3: Chuẩn hóa vector x
    x = x / x[p]

    while k <= N:
        # Step 5: Nhân ma trận A với vector x
        y = np.dot(A, x)

        # Step 6: Tìm chỉ số của phần tử có giá trị tuyệt đối lớn nhất trong y
        p = np.argmax(np.abs(y))
        mu = y[p]

        # Step 9: Tính sai số
        ERR = np.linalg.norm(x - y / y[p], np.inf)

        # Step 10: Kiểm tra sai số so với ngưỡng TOL
        if ERR < TOL:
            return mu, x

        # Step 7: Chuẩn hóa lại vector x
        x = y / y[p]

        # Step 11: Tăng biến đếm k
        k += 1

    print("Số lần lặp tối đa đã vượt quá")
    return None, None

# Ví dụ sử dụng Power Method
A = np.array([[4, 1],
              [2, 3]])

x = np.array([1, 1])
TOL = 1e-6
N = 100

mu, eigenvector = power_method(A, x, TOL, N)

print(f"Giá trị riêng: {mu}")
print(f"Vector riêng: {eigenvector}")

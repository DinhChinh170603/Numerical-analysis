import numpy as np

# Định nghĩa ma trận A và các vectơ x, b
A = np.array([[1, 2, 0, 3], # A là ma trận tiêu thụ thức ăn của từng loài.
              [1, 0, 2, 2],
              [0, 0, 1, 1]], dtype=float)
x = np.array([1000, 500, 350, 400], dtype=float) #là vectơ số lượng từng loài động vật.
b = np.array([3500, 2700, 900], dtype=float) #là vectơ tổng lượng thức ăn có sẵn hàng ngày.

# a. Kiểm tra nếu đủ thức ăn để đáp ứng tiêu thụ trung bình hàng ngày
Ax = A @ x #Tính tích
sufficient_food = np.allclose(Ax, b) #kiểm tra gần bằng
print("Có đủ thức ăn để đáp ứng tiêu thụ trung bình hàng ngày:", sufficient_food)

# b. Tìm số lượng tối đa của mỗi loài động vật có thể được thêm vào hệ thống mà vẫn đáp ứng đủ thức ăn
max_animals = np.floor(b / np.sum(A, axis=1)) #np.floor(): làm tròn xuống (lấy phần nguyên) #Chia từng phần tử của b cho tổng lượng tiêu thụ của từng loài (tổng các hàng của A)
print("Số lượng tối đa của mỗi loài động vật có thể được thêm vào:", max_animals)

# c. Nếu loài 1 tuyệt chủng, tính lượng tăng của các loài còn lại có thể được hỗ trợ
A_without_species_1 = A[:, 1:]
x_without_species_1 = np.linalg.pinv(A_without_species_1) @ b #Giả nghịch đảo Moore-Penrose #Bỏ cột của loài 1 trong ma trận A
# -> Giải hệ phương trình mới để tìm số lượng các loài còn lại.
print("Lượng tăng của các loài còn lại nếu loài 1 tuyệt chủng:", x_without_species_1)

# d. Nếu loài 2 tuyệt chủng, tính lượng tăng của các loài còn lại có thể được hỗ trợ
A_without_species_2 = np.delete(A, 1, axis=1) #Bỏ cột của loài 2 trong ma trận A
# -> Giải hệ phương trình mới để tìm số lượng các loài còn lại.
x_without_species_2 = np.linalg.pinv(A_without_species_2) @ b #Giả nghịch đảo Moore-Penrose
print("Lượng tăng của các loài còn lại nếu loài 2 tuyệt chủng:", x_without_species_2)

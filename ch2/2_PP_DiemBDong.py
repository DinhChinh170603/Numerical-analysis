import math

# Định nghĩa hàm g(x) theo bài toán
def g(x):
    return math.cos(x)

# Phương pháp điểm bất động
def fixpoint_method(p0, TOL, max_iteration):
    """
    Phương pháp điểm bất động để tìm nghiệm của phương trình f(x) = 0 bằng cách sử dụng g(x)
    :param p0: Giá trị ban đầu
    :param TOL: Ngưỡng sai số cho phép
    :param max_iteration: Số lần lặp tối đa
    :return: Nghiệm tìm được
    """
    i = 1  # Khởi tạo bộ đếm vòng lặp

    while i <= max_iteration:
        p = g(p0)  # Tính giá trị mới từ hàm g(x)
        print(f'Vòng lặp thứ {i}:')
        print(f'p0 = {p0:.10f} -> p = {p:.10f}')  # Chỉ in 10 chữ số sau dấu phẩy

        # Kiểm tra điều kiện dừng của thuật toán
        if abs(p - p0) < TOL:
            print(f'Kết quả: p = {p:.10f}')
            return p  # Trả về nghiệm nếu tìm thấy

        p0 = p  # Cập nhật giá trị p0 cho lần lặp tiếp theo
        i += 1  # Tăng bộ đếm vòng lặp

    print('Thất bại sau', max_iteration, 'vòng lặp')
    return None

# Khởi tạo các tham số
p0 = 0.5  # Giá trị ban đầu
TOL = 1e-5  # Ngưỡng sai số chấp nhận được
max_iteration = 100  # Số lần lặp tối đa

# Gọi hàm fixpoint_method để thực hiện phương pháp điểm bất động
fixpoint_method(p0, TOL, max_iteration)

def func(x):
    return x ** 2 - 6  # Hàm số f(x) = x^2 - 6

# Tham số khởi tạo
p0 = 3  # Giá trị ước lượng ban đầu p0
p1 = 2  # Giá trị ước lượng ban đầu p1
TOL = 1e-6  # Sai số chấp nhận được
max_iteration = 1e6  # Số lần lặp tối đa

def secant_method(p0, p1, TOL, max_iteration):
    i = 2  # Bắt đầu từ lần lặp thứ hai, theo thuật toán
    q0 = func(p0)  # Tính f(p0)
    q1 = func(p1)  # Tính f(p1)

    while i <= max_iteration:  # Tiếp tục lặp nếu chưa đạt số lần lặp tối đa
        p = p1 - q1 * (p1 - p0) / (q1 - q0)  # Tính giá trị mới p theo công thức Secant
        # với q0 và q1 là các giá trị của hàm tại p0 và p1. Đây là phương pháp gần đúng để tìm nghiệm của phương trình phi tuyến không cần đạo hàm.
        if abs(p - p1) < TOL:  # Kiểm tra điều kiện dừng của thuật toán
            print(f'kết quả: p = {p}')
            return p  # Trả về nghiệm nếu tìm thấy

        # Cập nhật giá trị cho lần lặp tiếp theo
        p0 = p1
        q0 = q1
        p1 = p
        q1 = func(p)

        i += 1  # Tăng bộ đếm vòng lặp

    print(f'thất bại sau {i} vòng lặp')  # In thông báo thất bại nếu vượt quá số lần lặp

secant_method(p0, p1, TOL, max_iteration)

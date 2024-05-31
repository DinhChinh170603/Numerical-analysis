def func(x):
    return x ** 2 - 6  # Hàm số f(x) = x^2 - 6

p0 = 3  # Giá trị ước lượng ban đầu p0
p1 = 2  # Giá trị ước lượng ban đầu p1
TOL = 1e-6  # Sai số chấp nhận được
max_iteration = 1e6  # Số lần lặp tối đa

def false_position_method(p0, p1, TOL, max_iteration):
    i = 2  # Bắt đầu từ lần lặp thứ hai, theo thuật toán
    q0 = func(p0)  # Tính f(p0)
    q1 = func(p1)  # Tính f(p1)

    while i <= max_iteration:  # Tiếp tục lặp nếu chưa đạt số lần lặp tối đa
        p = p1 - q1 * (p1 - p0) / (q1 - q0)  # Tính giá trị mới p theo công thức False Position
        #sử dụng giá trị hàm tại p0 và p1 để ước lượng nghiệm.
        if abs(p - p1) < TOL:  # Kiểm tra điều kiện dừng của thuật toán
            # Kiểm tra xem giá trị mới p có đủ gần với ước lượng trước đó p1 không. Nếu khoảng cách nhỏ hơn hoặc bằng sai số cho phép, thuật toán dừng lại và trả về nghiệm.
            print(f'kết quả: p = {p}')
            return p  # Trả về nghiệm nếu tìm thấy

        q = func(p)  # Tính f(p) mới

        if q * q1 < 0:  # Cập nhật giá trị p0, q0 nếu f(p) và f(p1) trái dấu
            # nếu không, chỉ cập nhật p1 và q1.
            p0 = p1
            q0 = q1

        p1 = p  # Cập nhật p1 và q1 cho lần lặp tiếp theo
        q1 = q

        i += 1  # Tăng bộ đếm vòng lặp

    print(f'thất bại sau {i} vòng lặp')  # In thông báo thất bại nếu vượt quá số lần lặp

false_position_method(p0, p1, TOL, max_iteration)

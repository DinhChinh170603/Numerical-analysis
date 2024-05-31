def func(x):
    return x ** 2 - 6  # Hàm số f(x) = x^2 - 6

def diff_func(x):
    return (func(x + 1e-9) - func(x)) / (1e-9)  # Đạo hàm số f(x) sử dụng sai phân tiến

# Tham số khởi tạo
p0 = 1  # Giá trị ước lượng ban đầu
TOL = 1e-6  # Sai số chấp nhận được
max_iteration = 1e6  # Số lần lặp tối đa

def newton_method(p0, TOL, max_iteration):
    i = 1  # Khởi tạo bộ đếm vòng lặp

    while i <= max_iteration:  # Tiếp tục lặp nếu chưa đạt số lần lặp tối đa
        p = p0 - func(p0) / diff_func(p0)  # Tính giá trị mới p theo phương pháp Newton #func là f(x), diff_func là f'(x)
        # f'(p0) được tính bằng phương pháp sai phân tiến.
        if abs(p - p0) < TOL:  # Kiểm tra điều kiện dừng của thuật toán
            print(f'kết quả: p = {p}')
            return p  # Trả về nghiệm nếu tìm thấy
        # Kiểm tra xem giá trị mới p có đủ gần với ước lượng trước đó p0 không. 
        # Nếu khoảng cách nhỏ hơn hoặc bằng sai số cho phép, thuật toán dừng lại và trả về nghiệm.

        i += 1  # Tăng bộ đếm vòng lặp
        p0 = p  # Cập nhật giá trị p0 cho lần lặp tiếp theo

    print(f'thất bại sau {i} vòng lặp')  # In thông báo thất bại nếu vượt quá số lần lặp

newton_method(p0, TOL, max_iteration)

#
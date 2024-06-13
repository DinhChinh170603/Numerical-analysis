def mortgage_payment(P, i, n):
    return P / i * (1 - (1 + i)**-n)

def find_max_interest_rate(A, P, n, tol=1e-10):
    low, high = 0, 1  # Lãi suất thấp nhất và cao nhất
    while high - low > tol:
        mid = (low + high) / 2
        if mortgage_payment(P, mid, n) < A:
            low = mid
        else:
            high = mid
    return low

# Khởi tạo các giá trị
A = 135000  # Số tiền vay
P = 1000    # Số tiền trả hàng tháng
n = 30 * 12 # Số lần thanh toán

# Tìm lãi suất tối đa
max_interest_rate = find_max_interest_rate(A, P, n)
annual_interest_rate = max_interest_rate * 12 * 100  # Chuyển đổi sang lãi suất hàng năm

print(f'Lãi suất hàng tháng tối đa: {max_interest_rate}')
print(f'Lãi suất hàng năm tối đa: {annual_interest_rate:.6f}%')

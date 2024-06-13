def g_a(x):
    return 0.5 * x + 1  # Hàm giả định thỏa mãn g'(x) <= k

def g_a_prime(x):
    return 0.5  # Đạo hàm của g_a(x)

# Kiểm tra duy nhất của điểm bất động
def check_uniqueness(f, df, a, b, tol=1e-6):
    x1 = a
    x2 = b
    while abs(x1 - x2) > tol:
        x1 = f(x1)
        x2 = f(x2)
        if abs(x1 - x2) < tol:
            return True  # Duy nhất
    return False  # Không duy nhất

# Kiểm tra hàm g_a
print("Hàm g_a có duy nhất một điểm bất động:", check_uniqueness(g_a, g_a_prime, 0, 1))

import numpy as np

points = np.array([[1, 2], [2, 4], [3, 6]])

approx_point = 7

def divided_differences(points: np.ndarray):
    n = points.shape[0]

    result = np.ndarray()

    f = np.empty([n + 1, n + 1])
    
    for i in range(n + 1):
        f[i][0] = points[i][1]
        print(f[i][0])

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            f[i][j] = (f[i][j - 1] - f[i - 1][j - 1]) / (points[0][i] - points[0][i - j])

    return f
def newton_interpolation_forward(points: np.ndarray, approx_point):
    pass

print(newton_interpolation_forward(points, approx_point))
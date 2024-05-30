import numpy as np

points = np.array([[1, 2], [2, 4], [3, 6]])

approx_point = 7

def lagrange_interpolation(points: np.ndarray, approx_point):
        
        n = points.shape[0]
        result = 0

        for i in range(n):
            numerator = np.multiply.reduce([ approx_point - points[j][0] for j in range(n) if j != i])
            denominator = np.multiply.reduce([ points[i][0] - points[j][0] for j in range(n) if j != i ])

            result += points[i][1] * numerator / denominator

        return result

print(lagrange_interpolation(points, approx_point))
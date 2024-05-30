import numpy as np

# datapoint
x = np.array([4.0, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1])
y = np.array([102.56, 113.18, 130.11, 142.05, 167.53, 195.14, 224.87, 256.73, 299.50, 326.72])

def augmented_matrix_cal(x: np.ndarray, y: np.ndarray, degree=2, discrete=True):

    coefficient = np.empty([degree + 1, degree + 1])

    if discrete:
        # Create the Vandermonde matrix for calculation
        V = np.vander(x, degree * 2 + 1, increasing=True)
        # print(V)

        # get coefficients values
        coefficienct_values = np.sum(V, axis=0)
        # print(coefficienct_values)

        # map it to result
        for i in range(degree + 1):
            coefficient[i] = coefficienct_values[i: i + degree + 1]
        # print(coefficient)

        x_pow_n_values = V[:,:degree + 1]
        dependent_vars = np.dot(y, x_pow_n_values)
        
    else:
        return None

    return coefficient, dependent_vars

coefficients, dependent_vars = augmented_matrix_cal(x, y, 3)

# least square
result, _, _, _ = np.linalg.lstsq(coefficients, dependent_vars, rcond=None)

print(result)
import math
import numpy as np

# # change the function
# def X(x):
#     return x

# def Y(y):
#     return y

# def A(a):
#     return a

# def B(x):
#     return B
float_formatter = "{:.2f}".format
np.set_printoptions(formatter={'float_kind':float_formatter})

degree = 3

x_list = np.array([4.0, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1])
y_list = np.array([102.56, 113.18, 142.05, 167.53, 195.14, 224.87, 299.50, 326.72])
n = x_list.size

def power_of_n(data, n):
  # Calculate maximum power width
  max_power_width = len(max(f"x^{i}" for i in range(1, 2*n + 1)))

  # Create header row with powers as labels (excluding element)
  header = [f"x^{i}" for i in range(1, 2*n + 1)]

  # Print header row with formatting
  print(" " * int(max_power_width / 2), end="")
  print(" ".join([p.rjust(max_power_width) for p in header]))
  print("-" * (sum(max_power_width for _ in header)))

  # Create a NumPy array to store powers (initialize with zeros)
  powers = np.zeros((data.size, 2*n))

  # Iterate over elements and print powers in table format (excluding element)
  for i in range(data.size):
    x = data.flat[i]
    row = []
    for j in range(1, 2*n + 1):
      powers[i, j-1] = round(x**j, 2)
      row.append(f"{powers[i, j-1]:.2f}")
    print(" " * int(max_power_width / 2), end="")
    print(" ".join(row))

  return powers  # Return powers excluding first column

# Example usage
left_side = power_of_n(x_list, 3)
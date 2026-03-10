import numpy as np

print("----- Basic Matrix Operation -----")

# Matrix A and B
A = np.array([[2, 3],
              [1, 4]])

B = np.array([[5, 6],
              [3, 1]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Addition
add_result = A + B
print("Addition (A + B):\n", add_result)

# Multiplication
mul_result = np.dot(A, B)
print("Multiplication (A x B):\n", mul_result)

# Transpose
transpose_A = A.T
print("Transpose of A:\n", transpose_A)

# Inverse
inverse_A = np.linalg.inv(A)
print("Inverse of A:\n", inverse_A)


print("\n----- Test Case 1 -----")

A1 = np.array([[1, 2],
               [3, 4]])

B1 = np.array([[2, 0],
               [1, 2]])

print("Matrix A1:\n", A1)
print("Matrix B1:\n", B1)

result_test1 = np.dot(A1, B1)

print("Result of Test Case 1:\n", result_test1)


print("\n----- Test Case 2 -----")

A2 = np.array([[1, 2],
               [3, 4],
               [5, 6]])

B2 = np.array([[1, 0, 1],
               [0, 1, 0]])

print("Matrix A2:\n", A2)
print("Matrix B2:\n", B2)

result_test2 = np.dot(A2, B2)

print("Result of Test Case 2:\n", result_test2)


print("\n----- Traffic Flow Simulation -----")

# Traffic flow matrix
F = np.array([[50, 20],
              [30, 40]])

# Transformation matrix
T = np.array([[0.8, 0.2],
              [0.3, 0.7]])

print("Original Traffic Matrix:\n", F)
print("Transformation Matrix:\n", T)

new_flow = np.dot(F, T)

print("New Traffic Distribution After Optimization:\n", new_flow)
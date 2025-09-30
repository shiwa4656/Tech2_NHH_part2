#! C:\Users\shirw\OneDrive\Documents\Tech2_NHH_part2\testN\Scripts\python.exe

import numpy as np

# Create a simple array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Basic operations
print("Add 10:", arr + 10)
print("Multiply by 2:", arr * 2)

# Array of zeros and ones
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
print("Zeros:\n", zeros)
print("Ones:\n", ones)

# Random numbers
rand_nums = np.random.rand(3, 3)
print("Random 3x3:\n", rand_nums)

# Statistics
print("Mean:", arr.mean())
print("Sum:", arr.sum())
print("Standard Deviation:", arr.std())

# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Matrix Multiplication:\n", np.dot(A, B))

import numpy as np

# 1) What happens when we transpose twice? M = matrix, MT = transpose, MTT = matrix transpose transpose
# 2) confirm that the transpose operation works on non-square matrices

M = np.round(5 * np.random.randn(3,4))
Mt = M.T

print("Matrix")
print(M)
print(" ")
print("Matrix Transpose")
print(Mt)
print(" ")
print("Matrix Transpose Transpose")
print(Mt.T)

print(" ")
M2 = np.array([[1,5,2], [4,5]], dtype=object)
print(M2)
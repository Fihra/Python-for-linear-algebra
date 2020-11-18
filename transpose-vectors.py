import numpy as np

#Transpose for a vector

# np.array takes 2nd optional arguments
# ndim = number of dimensions
v1 = np.array([2,3,-1], ndmin=2)

print(v1)
print(' ')
print(v1.T)

#Transpose for a matrix
M = np.round(10 * np.random.randn(3,3))
print(M)
print(' ')
print(M.T)
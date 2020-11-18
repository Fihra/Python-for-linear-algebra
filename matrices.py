import numpy as np

#Identity Matrix
# print(np.eye(5))

#Matrix of all 0s
zero = np.zeros((3, 4))
# print(zero)

#Create a matrix where we specify the size, then specify number to fill the matrix
print(np.full((5,2), 7))

M = np.array([[1,2,3], 
              [4,5,6], 
              [7,8,9]])
print(M)
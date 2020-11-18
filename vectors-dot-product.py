import matplotlib.pyplot as plt
import numpy as np

v1 = np.array([5, 6, 2])
v2 = np.array([3, 0, 5])

#Dot Product
print(np.dot(v1, v2))

v3 = np.array([-4,3,1])
print(np.dot(v2, v3))

v4 = np.array([0, 0, 0])
print(np.dot(v3, v4))

v5 = np.array([2, 3, -1])
print(np.dot(v3, v5))

#vector v3 is orthogonal to vector v5
#have a dot product of 0

import matplotlib.pyplot as plt 
import numpy as np

vec = np.array([3, 4, 5, 2])
s = 3

print(vec * s)

vec2d = np.array([1,2])
s1 = 2
s2 = .5
s3 = -1

#Plotting, x -> x, y -> y
plt.plot([0, vec2d[0]], [0, vec2d[1]], 'bs-')
plt.show()
import matplotlib.pyplot as plt
import numpy as np

vectors = np.array([3,4,5,2])
s = 3

print(str(vectors*s))

vector2d = np.array([1,2])
scalar1 = 2
scalar2 = .5
scalar3 = -1

# plt.plot([0, vector2d[0]], [0,vector2d[1]], 'bs-')
plt.plot([0, vector2d[0]], [0,vector2d[1]], 'bs-', label="v")
plt.plot([0, scalar1*vector2d[0]], [0,scalar1*vector2d[1]], 'ro-', label="v*s1")
plt.plot([0, scalar2*vector2d[0]], [0,scalar2*vector2d[1]], 'kp-', label="v*s2")
plt.plot([0, scalar3*vector2d[0]], [0,scalar3*vector2d[1]], 'g*-', label="v*s3")

plt.axis('square')
plt.xlim([-4,4])
plt.ylim([-4,4])
plt.grid()
plt.legend()

plt.show()
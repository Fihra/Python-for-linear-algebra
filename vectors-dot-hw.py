import matplotlib.pyplot as plt
import numpy as np

#1) come up with 3 2D vectors, two of them are ortagonal, but neither is ortagonal to the third
#2) plot all three vectors -- make sure the axes are square and equal

v1 = np.array([-3 , 2])
v2 = np.array([2, 3])

v3 = np.array([5, 1])

print(np.dot(v1, v2))
print(np.dot(v1, v3))

plt.plot([0, v1[0]],[0, v1[1]], 'bs-', label="Vector 1")
plt.plot([0, v2[0]],[0,v2[1]], 'rs-', label="Vector 2")
plt.plot([0, v3[0]],[0, v3[1]], 'gs-', label="Vector 3")

plt.axis('square')
plt.xlim([-5,5])
plt.ylim([-5,5])

plt.legend()
plt.show()
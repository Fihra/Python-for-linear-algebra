#create 2 vectors (2D vectors)
#random or your own
#plot each vector
#plot v1 + v2, v1-v2, (v1*4 + v2/2)

import matplotlib.pyplot as plt
import numpy as np

nums = np.random.randint(0, 10, size=[1, 4])

v = np.array(nums[0])

print(v)

plt.plot([v[0],v[0] + v[2]], [v[1],v[1] + v[3]], 'bo-', label="Vector 1")
plt.plot([v[0], v[0] - v[2]], [v[1],v[1] - v[3]], 'ro-', label="Vector 2")
plt.plot([v[0], v[0]*4 + v[2]/2], [v[1], v[1]*4 + v[3]/2], 'go-', label='Vector 3')

plt.legend()
plt.show()
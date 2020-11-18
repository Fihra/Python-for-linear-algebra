import matplotlib.pyplot as plt
import numpy as np

#Create 2 Vectors (2D vectors)
#plot each vector
#plot v1 + v2, v1 - v2, v1 * 4, v2 /2

def randomNumbers():
    return np.random.randint(0, 10, size=[1, 2])

def convertToArray(nums):
    return np.array(nums[0])

nums1 = randomNumbers()
nums2 = randomNumbers()
vector1 = convertToArray(nums1)
vector2 = convertToArray(nums2)
print(vector1)
print(vector2)

# v1 + v2
plt.plot([vector1[0], vector1[0] + vector2[0]], [vector1[1], vector1[1] + vector2[1]], 'bs-', label="Vector 1")

# v1 - v2
plt.plot([vector1[0], vector1[0] - vector2[0]], [vector1[1], vector1[1] - vector2[1]], 'rs-', label="Vector 2")

# v1 * 4
plt.plot([vector1[0], vector1[0] * 4], [vector1[1], vector1[1] * 4], 'go-', label="Vector 3")

# v2 / 2
plt.plot([vector2[0], vector2[0]/2], [vector2[1], vector2[1]/2], 'yo-', label="Vector 4")

plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

M = np.random.randint(0, 10, size=(4,5))
print(M)

plt.imshow(M)
plt.show()
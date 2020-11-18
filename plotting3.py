# Import modules
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-9, 10)
print(x)

y = x**2
print(y)

#plotting x, y, color/shape
# plt.plot(x, y, 'r')
# plt.plot(x, y/2, 'gs')

#To draw a line
# 2 x coordinates, 2 y coordinates
# 0 -> 3 on x axis
# -1 -> 1 on y axis

# IN X/Y Format = (0, -1) -> (3, 1) 

plt.plot([0,3],[-1,1], label='first line')
plt.plot([-2,0], [-4,1], label='second line')

#Activate the legend
plt.legend()

plt.show()
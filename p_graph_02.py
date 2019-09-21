# 散布図

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4])
y = np.array([12, 36, 7, 85, 54])

plt.scatter(x, y, color = "r")
plt.show()

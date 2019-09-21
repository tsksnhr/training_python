# 2つの曲線

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 300)
y0 = x**2
y1 = (x-5)**2

plt.plot(x, y0, color = "r")
plt.plot(x, y1, color = "b", linestyle = "--")

plt.show()

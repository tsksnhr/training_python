# 曲線グラフ

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 300)
y = x**2

print(x)
print(y)

plt.plot(x, y, color = "r")
plt.show()
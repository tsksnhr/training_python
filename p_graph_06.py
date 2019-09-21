import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 300)
sin_x = np.sin(x)
cos_x = np.cos(x)

fig, axes = plt.subplots(2, 1)
print("fig = {}".format(fig))
print("axes = {}".format(axes))

axes[0].set_ylim([-1.5, 1.5])
axes[1].set_ylim([-1.5, 1.5])
axes[0].plot(x, sin_x, color = "r")
axes[1].plot(x, cos_x, color = "b")

plt.show()

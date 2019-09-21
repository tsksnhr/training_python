import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x**2 + y**2 / 4

x = np.linspace(-5, 5, 300)
y = np.linspace(-5, 5, 300)

xmesh, ymesh = np.meshgrid(x, y)

z = f(xmesh.ravel(), ymesh.ravel()).reshape(xmesh.shape)        # 2次元配列を1次元配列にreshapeしてから、再び2次元配列としている(.shapeは行列のサイズを返す)

"""
plt.contourf(x, y, z, colors = "r", levels = [1, 2, 3, 4, 5])
plt.show()
"""

colors = ["0.1", "0.3", "0.5", "0.7"]                           # colorsの要素数はlevelsの配置より一つ少なくする(間の色を塗るから)
levels = [1, 2, 3, 4, 5]
plt.contourf(x, y, z, color = colors, levels = levels)
plt.show()

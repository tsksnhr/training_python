import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

xmesh, ymesh = np.meshgrid(x, y)

print(xmesh)
print(ymesh)

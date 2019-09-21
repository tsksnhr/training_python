import p_ml_06
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


# ベクトルのリッジ回帰
x = np.array([1, 2, 4, 6, 7])
y = np.array([1, 3, 3, 5, 4])
model = p_ml_06.RidgeRegression()
model.fit(x, y)
b, a = model.w_

print("--- 1 ---")
print(model.w_)
print()

plt.scatter(x, y, color = "k")
xmax = x.max()
plt.plot([0, xmax], [b, b + a*xmax], color = "k")
plt.show()

# 特徴量ベクトルが2次元の時のリッジ回帰
n = 100
scale = 10

np.random.seed(0)
X = np.random.random((n, 2))*scale
w0 = 1
w1 = 2
w2 = 3
y = w0 + w1*X[:, 0] + w2*X[:, 1] + np.random.randn(n)

model = p_ml_06.RidgeRegression()
model.fit(X, y)

xmesh, ymesh = np.meshgrid(np.linspace(0, scale, 20), np.linspace(0, scale, 20))
zmesh = (model.w_[0] + model.w_[1]*xmesh.ravel() + model.w_[2]*ymesh.ravel()).reshape(xmesh.shape)

print("--- 2 ---")
print(model.w_)
print()

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
ax.scatter(X[:, 0], X[:, 1], y, color = "k")
ax.plot_wireframe(xmesh, ymesh, zmesh, color = "r")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import p_ml_03                              # 自作したモジュールのimport

n = 100
scale = 10

np.random.seed(0)                           # 乱数のseedを設定
X = np.random.random((n, 2))*scale          # n行2列の行列を乱数で作成し、scale倍している(ブロードキャスティング)
w0 = 1
w1 = 2
w2 = 3
y = w0 + w1*X[:, 0] + w2*X[:, 1] + np.random.randn(n)       # Xの1行目、2行目をそれぞれ抜き出してw1倍、w2倍し、さらに乱数・w0と和を取っている

model = p_ml_03.LinearRegression()
model.fit(X, y)
print("係数： ", model.w_)
print("(1, 1)に対する予測値： ", model.predict(np.array([1, 1])))

xmesh, ymesh = np.meshgrid(np.linspace(0, scale, 20), np.linspace(0, scale, 20))
zmesh = (model.w_[0] + model.w_[1]*xmesh.ravel() + model.w_[2]*ymesh.ravel()).reshape(xmesh.shape)

print("model.w_ = ", model.w_)
print("model.w_[0] = ", model.w_[0])
print("model.w_[1] = ", model.w_[1])
print("model.w_[2] = ", model.w_[2])

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
ax.scatter(X[:, 0], X[:, 1], y, color = "k")
ax.plot_wireframe(xmesh, ymesh, zmesh, color = "r")

plt.show()

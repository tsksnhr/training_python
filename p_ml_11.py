import numpy as np
import p_ml_03_LinearReg
import p_ml_10_PolynomialReg
import matplotlib.pyplot as plt

np.random.seed(0)

def f(x):
    return 1 + 2*x

x = np.random.random(10)*10         # 乱数を生成して10倍
y = f(x) + np.random.randn(10)      # xをf(x)に代入した値に乱数でノイズを載せている

# 多項式回帰
model = p_ml_10_PolynomialReg.PolynomialRegression(10)        # 10乗まで考えた多項式回帰
model.fit(x, y)

plt.scatter(x, y, color = "b")
plt.ylim([y.min() - 1, y.max() + 1])            # グラフの表示範囲をyの最大最小の+-1までに限定

xx = np.linspace(x.min(), x.max(), 300)         # xの最大最小の間を300分割
yy = np.array([model.predict(u) for u in xx])   # xxの値それぞれについて多項式回帰で予測した値をyyに配列として格納
plt.plot(xx, yy, color = "r")

# 線形回帰
model = p_ml_03_LinearReg.LinearRegression()
model.fit(x, y)
b, a = model.w_

x1 = x.min() - 1
x2 = x.max() + 1
plt.plot([x1, x2], [f(x1), f(x2)], color = "k", linestyle = "dashed")

plt.show()

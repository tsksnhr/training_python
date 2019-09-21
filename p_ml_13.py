import numpy as np
import matplotlib.pyplot as plt
import warnings
import p_ml_03_LinearReg      # 線形回帰
import p_ml_10_PolynomialReg      # 多項式回帰

def f(x):
    return 1/(1 + x)

def sample(n):
    x = np.random.random(n)*5
    y = f(x)
    return x, y

xx = np.arange(0, 5, 0.01)          # 0~5まで0.01刻みで1次元配列に格納
np.random.seed(0)

y_poly_sum = np.zeros(len(xx))      # xxと同じ要素数の零ベクトルを作成
y_poly_sum_sq = np.zeros(len(xx))   # xxと同じ要素数の零ベクトルを作成
y_lin_sum = np.zeros(len(xx))       # xxと同じ要素数の零ベクトルを作成
y_lin_sum_sq = np.zeros(len(xx))    # xxと同じ要素数の零ベクトルを作成
y_true = f(xx)

n = 100000

warnings.filterwarnings("ignore")

for i in range(n):
    x, y = sample(5)
    poly = p_ml_10_PolynomialReg.PolynomialRegression(4)      # 4次の多項式近似
    poly.fit(x, y)

    lin = p_ml_03_LinearReg.LinearRegression()            # 線形近似
    lin.fit(x, y)

    y_poly = poly.predict(xx)
    y_poly_sum += y_poly                        # 多項式近似による予測値の合計
    y_poly_sum_sq += (y_poly - y_true)**2       # 予測値と真値の差の2乗の合計

    y_lin = lin.predict(xx.reshape(-1, 1))
    y_lin_sum += y_lin                          # 線形近似による予測値の合計
    y_lin_sum_sq += (y_lin - y_true)**2         # 予測値と真値の差の2乗の合計

fig = plt.figure()

ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.set_title("Linear Reg.")
ax2.set_title("Polynomial Reg.")

ax1.set_ylim(0, 1)
ax2.set_ylim(0, 1)

# fill_betweeは引数に取った関数、数値の間を塗りつぶす関数
ax1.fill_between(xx, 0, (y_lin_sum/n - y_true)**2, color = "0.2", label = "bias")                       # 予測値の平均と真値の差の2乗をグラフ化
ax1.fill_between(xx, (y_lin_sum/n - y_true)**2, y_lin_sum_sq/n, color = "0.7", label = "variance")      # 予測値の誤差の2乗値とbiasの差からvarianceを導出
ax1.legend(loc = "upper left")

ax2.fill_between(xx, 0, (y_poly_sum/n - y_true)**2, color = "0.2", label = "bias")                      # 予測値の平均と真値の差の2乗をグラフ化
ax2.fill_between(xx, (y_poly_sum/n - y_true)**2, y_poly_sum_sq/n, color = "0.7", label = "variance")    # 予測値の誤差の2乗値とbiasの差からvarianceを導出
ax2.legend(loc = "upper left")

plt.show()

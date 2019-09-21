import numpy as np
import matplotlib.pyplot as plt
import warnings
import p_ml_03_LinearReg      # 線形回帰
import p_ml_10_PolynomialReg      # 多項式回帰

def f(x):
    return 1/(1 + x)

def sample(n):
    x = np.random.random(n)*5           # 0～1の乱数を生成し、それぞれを5倍している
    y = f(x)                            # 上で定義した f(x)=1/(1+x)に5つの乱数を代入している
    return x, y                         # 乱数xとf(x)がそれぞれ戻り値x,yとなる

xx = np.arange(0, 5, 0.01)              # 0.01刻みで0から4.99まで1次元配列として格納
np.random.seed(0)
y_poly_sum = np.zeros(len(xx))          # 配列xxの要素数だけの次元の零行列(ここでは零ベクトル、引数が一つなので)を作成
y_lin_sum = np.zeros(len(xx))           # 配列xxの要素数だけの次元の零行列(ここでは零ベクトル、引数が一つなので)を作成
n = 100000

warnings.filterwarnings("ignore")

for _ in range(n):
    x, y = sample(5)                            # 乱数5個を生成し、それに応じたf(x)の値を戻り値として返している
    poly = p_ml_10_PolynomialReg.PolynomialRegression(4)      # 4次の多項式回帰
    poly.fit(x, y)

    lin = p_ml_03_LinearReg.LinearRegression()            # 線形回帰
    lin.fit(x, y)                               # 学習

    y_poly = poly.predict(xx)                   # 予測(予測値はy_poly)
    y_poly_sum += y_poly                        # 予測値の和を取る(1次元配列の足し算)

    y_lin = lin.predict(xx.reshape(-1, 1))      # 予測(予測値はy_lin)
    y_lin_sum += y_lin                          # 予測値の和を取る(1次元配列の足し算)

print(y_poly_sum)
print(y_lin_sum)

plt.plot(xx, f(xx), label = "truth", color = "k", linestyle = "solid")                      # 真値をグラフ化
plt.plot(xx, y_poly_sum/n, label = "polynominal reg.", color = "r", linestyle = "dotted")   # 多項式回帰の予測値の平均をグラフ化
plt.plot(xx, y_lin_sum/n, label = "linear reg.", color = "b", linestyle = "dashed")         # 線形回帰の予測値の平均をグラフ化

plt.legend()        # ラベルを凡例として表示
plt.show()

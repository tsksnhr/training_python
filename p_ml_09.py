import numpy as np
import matplotlib.pyplot as plt
import p_ml_03_LinearReg
import p_ml_06_RidgeReg

x = np.arange(12)
y = 1 + 2*x
y[2] = 20
y[4] = 0

xmin = 0
xmax = 12
ymin = -1
ymax = 25

fig, axes = plt.subplots(nrows = 2, ncols = 5)      # 2*5でグラフを一つのウィンドウに生成

for i in range(5):
    axes[0, i].set_xlim([xmin, xmax])               # 1行目のグラフのx軸の最大、最小を決定  
    axes[0, i].set_ylim([ymin, ymax])               # 1行目のグラフのy軸の最大、最小を決定
    axes[0, i].set_xlim([xmin, xmax])               # 2行目のグラフのx軸の最大、最小を決定
    axes[0, i].set_ylim([ymin, ymax])               # 2行目のグラフのy軸の最大、最小を決定

    xx = x[:2 + i*2]                                # リストxの先頭からxxに格納する数値の数を増やしている
    yy = y[:2 + i*2]                                # リストyの先頭からyyに格納する数値の数を増やしている 

    # 同じ列のグラフに同じ散布図を生成
    axes[0, i].scatter(xx, yy, color = "k")
    axes[1, i].scatter(xx, yy, color = "k")

    # 線形回帰
    model = p_ml_03_LinearReg.LinearRegression()              
    model.fit(xx, yy)                               
    xs = [xmin, xmax]
    ys = [model.w_[0] + model.w_[1]*xmin, model.w_[0] + model.w_[1]*xmax]
    axes[0, i].plot(xs, ys, color = "k")

    # リッジ回帰
    model = p_ml_06_RidgeReg.RidgeRegression()               
    model.fit(xx, yy)
    xs = [xmin, xmax]
    ys = [model.w_[0] + model.w_[1]*xmin, model.w_[0] + model.w_[1]*xmax]
    axes[1, i].plot(xs, ys, color ="k")

plt.show()

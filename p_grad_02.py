import numpy as np
import matplotlib.pyplot as plt
import p_grad_01                    # 自作したクラスGradientDscentを使用するためにモジュールをインポート

def f(xx):                          # 問題の関数を定義
    x = xx[0]
    y = xx[1]
    return 5 * x**2 - 6 * x * y + 3 * y**2 + 6 * x - 6 * y

def df(xx):                         # 導関数を定義
    x = xx[0]
    y = xx[1]
    return np.array([10 * x - 6 * y + 6, -6 * x + 6 * y - 6])

algo = p_grad_01.GradientDescent(f, df)                 # クラス呼び出し
initial = np.array([1, 1])                              # 初期値定義
algo.solve(initial)                                     # クラス内の関数を使用
print(algo.x_)                                          # 結果を表示
print(algo.opt_)                                        # 結果を表示

plt.scatter(initial[0], initial[1], color = "b", marker = "o")                  # グラフ中に初期値を表示
plt.plot(algo.path_[:, 0], algo.path_[:, 1], color = "r", linewidth = 1.5)      # 初期値から最適値までの線を描画

xs = np.linspace(-2, 2, 300)
ys = np.linspace(-2, 2, 300)
xmesh, ymesh = np.meshgrid(xs, ys)
xx = np.r_[xmesh.reshape(1, -1), ymesh.reshape(1, -1)]                          # 配列の結合(ここではxmeshとymeshを結合して2行300列の行列にしている？)
levels = [-3, -2.9, -2.8, -2.6, -2.4, -2.2, -2, -1, 0, 1, 2, 3, 4]

plt.contour(xs, ys, f(xx).reshape(xmesh.shape), levels = levels, colors = "k", linestyles = "dotted")

plt.show()

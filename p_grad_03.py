import numpy as np
import matplotlib.pyplot as plt
import p_grad_01

def f(xx):
    x = xx[0]
    y = xx[1]
    return 5 * x**2 - 6 * x * y + 3 * y**2 + 6 * x - 6 * y

def df(xx):
    x = xx[0]
    y = xx[1]
    return np.array([10 * x - 6 * y + 6, -6 * x + 6 * y - 6])

xmin, xmax, ymin, ymax = -3, 3, -3, 3

algos = []
initial = np.array([1, 1])

alphas = [0.1, 0.2]         # alphaが0.2の時にoverflowが2乗計算の部分でoverflowが発生する(小さすぎてfloat64で桁が足りなくなってる？)
#alphas = [0.1]             # alpha=0.1だけだと桁あふれによるruntimewarningは発生しない

for alpha in alphas:
    algo = p_grad_01.GradientDescent(f, df, alpha)
    algo.solve(np.array(initial))
    algos.append(algo)

xs = np.linspace(xmin, xmax, 300)
ys = np.linspace(ymin, ymax, 300)

xmesh, ymesh = np.meshgrid(xs, ys)
xx = np.r_[xmesh.reshape(1,-1), ymesh.reshape(1, -1)]

fig, ax = plt.subplots(1, 2)
levels = [-3, -2.9, -2.8, -2.6, -2.4, -2.2, -2, -1, 0, 1, 2, 3, 4]

#for i in range(1):                     # alpha=0.1だけの時用のfor条件
for i in range(2):
    ax[i].set_xlim((xmin, xmax))
    ax[i].set_ylim((ymin, ymax))
    ax[i].set_title("alpha = {}".format(alphas[i]))         # 「機械学習のエッセンス」に書いてあるこの行は誤記なので注意(alphaはリストではないため)
    ax[i].scatter(initial[0], initial[1], color = "k", marker = "o")
    ax[i].plot(algos[i].path_[:, 0], algos[i].path_[:, 1], color = "k", linewidth = 1.5)
    ax[i].contour(xs, ys, f(xx).reshape(xmesh.shape), levels = levels, colors = "k", linestyles = "dotted")

plt.show()

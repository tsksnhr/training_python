def newton1dim(f, df, x0, eps = 10e-6, max_iter = 1000):
    x = x0
    iter = 0
    while True:
        x_new = x - f(x)/df(x)          # ある点xkにおけるfの接線とx軸との交点を求めている
        if abs(x - x_new) < eps:        # xkとx(k+1)が十分に近い場合計算を終了する
            break
        x = x_new
        iter += 1
        if iter == max_iter:            # 繰り返し回数がMAXであれば終了
            break
    return x_new

def f(x):                               # 関数fを定義
    return x**3 - 5*x +1

def df(x):                              # 導関数f'を定義
    return 3*x**2 - 5

# 解が3つある(3次方程式なので)
print(newton1dim(f, df, 2))
print(newton1dim(f, df, 0))
print(newton1dim(f, df, -3))

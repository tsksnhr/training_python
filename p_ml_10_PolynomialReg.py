# 多項式回帰

import numpy as np
import p_ml_03_LinearReg

class PolynomialRegression:
    def __init__(self, degree):
        self.degree = degree

    def fit(self, x, y):
        x_pow = []                              # 空のリストを定義
        xx = x.reshape(len(x), 1)               # 2次元配列としての縦ベクトルに変換
        for i in range(1, self.degree + 1):
            x_pow.append(xx**i)                 # ベクトルxを0乗(=1)から指定したdegree乗までリストに追加する
        mat = np.concatenate(x_pow, axis = 1)   # degree乗まで格納したリスト(ベクトル)を横に結合して行列を作成
        linreg = p_ml_03_LinearReg.LinearRegression()     # 自作モジュールから線形回帰のクラスを呼び出し
        linreg.fit(mat, y)
        self.w_ = linreg.w_

    def predict(self, x):
        r = 0
        for i in range(self.degree + 1):
            r += (x**i)*self.w_[i]
        return r

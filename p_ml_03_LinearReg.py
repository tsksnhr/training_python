# 線形回帰

import numpy  as np
from scipy import linalg

class LinearRegression:         # 回帰は英語でregression
    def __init__(self):
        self.w_ = None

    def fit(self, X, t):
        Xtil = np.c_[np.ones(X.shape[0]), X] 
        A = np.dot(Xtil.T, Xtil)
        b = np.dot(Xtil.T, t)
        self.w_ = linalg.solve(A, b)

    def predict(self, X):
        if X.ndim == 1:                         # Xが1次元配列の場合、if内の処理を実行
            X = X.reshape(1, -1)                # 1次元配列を1行の2次元配列へ変換
        Xtil = np.c_[np.ones(X.shape[0]), X]    # Xの1列目に要素がすべて1の列を追加
        return np.dot(Xtil, self.w_)            # Xtilderと重みwのベクトル積を計算して、予測値としている

import numpy as np

a = np.arange(9).reshape(3, 3)
b = np.arange(3)

print(a)
print(b)
print("")

# 2次元配列と1次元配列の積は転置を自動でやってくれる(縦ベクトル、横ベクトルをpython側で解釈)
# ベクトルbが縦ベクトルであれば定義可能
print(np.dot(a, b))
# ベクトルbが横ベクトルであれば定義可能
print(np.dot(b, a))
print("")

# 2次元配列同士の場合、厳密に解釈される
print(b.reshape(3, 1))
print(np.dot(a, b.reshape(3, 1)))
# 下の計算は3*1行列と3*3行列の積なので定義できずエラー
# print(np.dot(b.reshape(3, 1), a))
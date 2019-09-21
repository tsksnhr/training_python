# 平均、分散、標準偏差

import numpy as np

x = np.array([21.9, 24.5, 23.4, 26.2, 15.3, 22.4, 21.8, 16.8, 19.9, 19.1, 21.9, 25.9, 20.9, 18.8, 22.1, 20.0, 15.0, 16.0, 22.2, 26.4, 26.0, 28.3, 18.7, 21.3, 22.5, 25.0, 22.0, 26.1, 25.6, 25.7])

m = x.sum() / len(x)                            # len(x)はxの要素数を戻り値として出す

s = np.sqrt((((x - m)**2).sum()) / len(x))      # x - m でブロードキャストしている、ブロードキャストされた配列の和をsum()で取得

print("average = {:.4f}".format(m))
print("srandard deviation = {:.4f}".format(s))

print("average = {:.4f}".format(x.mean()))
print("srandard deviation = {:.4f}".format(x.std()))
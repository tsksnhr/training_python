import numpy as np

a = np.array([[3, 1, 1],
                [1, 2, 1],
                [0, -1, 1]])

# 逆行列を求める
a_inv = np.linalg.inv(a)
print(a_inv)
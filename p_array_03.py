# LU分解によって1次方程式の解を求める

import numpy as np
from scipy import linalg

a = np.array([[3, 1, 1], [1, 2, 1], [0, -1, 1]])
b = np.array([1, 2, 3])

print(a)
print(b)

lu, p = linalg.lu_factor(a)             # 行列AをLU分解
answer = linalg.lu_solve((lu, p), b)    # 1次方程式の解を求める

print(answer)
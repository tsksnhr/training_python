import numpy as np

a = np.array([[3, 1, 1], [1, 2, 1], [0, -1, 1]])
b = np.array([1, 2, 3])

# 1次方程式の解を求める
answer = np.linalg.solve(a, b)
print(answer)
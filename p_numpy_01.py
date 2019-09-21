# numpyの配列

import numpy as np

# 引数にはリストが与えられる
a = np.array([2,3,5,7,9])
print(a[2])
print(a[1:4])
print(a[2:-1])
print(a.dtype)
print("---")

b = np.arange(5)
c = np.arange(1,3,0.2)
print(b)
print(b.dtype)
print("---")

print(c)
print(c.dtype)
print("---")

# 型を指定できる
d = np.arange(5, dtype = np.float64)
print(d)
print(d.dtype)
print("---")

e = np.arange(5, dtype = np.int64)
print(e)
print(e.dtype)
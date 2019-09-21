import numpy as np

a = np.arange(9).reshape(3, 3)
b = np.arange(4, 13).reshape(3, 3)

print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)

# 行列積を求めたい場合はnumpyクラスのdot関数、またはdotメソッドを用いる
print("--dot--")
print(np.dot(a,b))
print(a.dot(b))
print(a@b)
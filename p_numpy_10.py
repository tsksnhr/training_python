import numpy as np

a = np.arange(12.).reshape(4, 3)
b = np.arange(3.).reshape(1, 3)
c = np.arange(4.).reshape(4, 1)
d = np.arange(3.)

print(a)
print(b)
print(c)
print(d)

print("a+b")
print(a+b)
print("a*c")
print(a*c)
print("b-c")
print(b-c)
print("a+d")
print(a+d)

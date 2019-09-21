import numpy  as np

a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)

print("-a-")
print(a)
print("-b-")
print(b)
print("-ab-")
print(np.r_[a, b])
print("-abT-")
print(np.c_[a, b])

c = np.arange(3)
d = np.arange(3, 6)
print("-c-")
print(c)
print("-d-")
print(d)
print("-cd-")
print(np.r_[c, d])
print("-cdT-")
print(np.c_[c, d])

# 2次元配列と結合するには次元を統一する必要がある
print("-ac-")
print(np.r_[a, c.reshape(1, 3)])
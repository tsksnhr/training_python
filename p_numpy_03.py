import numpy as np

a = np.arange(15).reshape(3,5)

print("--a--")
print(a)
print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)

b = np.arange(4.)

print("--b--")
print(b)
print(b.shape)
print(b.ndim)
print(b.size)
print(b.dtype)

c = np.arange(15).reshape(3,-1)

print("--c--")
print(c)
print(c.ravel())
print(c)
print(c.reshape(-1))

d = np.arange(4.)

print("--d--")
print(d)
print(d.reshape(-1,1))
print(d.reshape(1,-1))
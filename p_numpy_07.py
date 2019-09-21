import numpy as np

a = np.arange(9).reshape(3, 3)

print(a)
print(a*3)
print((a == 5) | (a == 3))
print(a > 5)
print(np.exp(a))

print("---")

print(a**2)
b = np.array([i**2 for i in a])
print(b)

print("---")

print(a[a>5])
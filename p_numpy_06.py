import numpy as np

a = np.arange(11)
print(a)

print("sum = {}".format(a.sum()))
print("mean = {}".format(a.mean()))
print("max = {}".format(a.max()))
print("min = {}".format(a.min()))

print("")

b = np.arange(10).reshape(2,-1)
print(b)

print("sum = {}".format(b.sum()))
print("mean = {}".format(b.mean()))
print("max = {}".format(b.max()))
print("min = {}".format(b.min()))

print("")

print("sum = {}".format(b.sum(axis = 1)))
print("mean = {}".format(b.mean(axis = 1)))
print("max = {}".format(b.max(axis = 1)))
print("min = {}".format(b.min(axis = 1)))

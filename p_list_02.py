a = [1,2,3]
# b = a
b = a[:]

print("a = {}".format(a))
print("b = {}".format(b))
print("---")

b.append(4)
b.append(5)

print("a = {}".format(a))
print("b = {}".format(b))
print("---")
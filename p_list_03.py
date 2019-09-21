# リスト内包表記

a = [[],[],[]]

a[0].append(1)
a[1].append(1)
a[1].append(2)
a[2].append(1)
a[2].append(2)
a[2].append(3)

print("a = {}".format(a))

b = [ i**2 for i in range(5) ]
print("b = {}".format(b))

c = [ [i**2 + 10 * j for j in range(5)] for i in range(5) ]
print("c = {}".format(c))

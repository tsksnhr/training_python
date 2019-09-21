a = 1,2,3
print("a = {}".format(a))

b = a, (4,5,6)
print("b = {}".format(b))

c = a, ("x","y","z")
print("c = {}".format(c))

d = a, b, ("x","y","z")
print("d = {}".format(d))

# 下はエラーになる、タプルは不変型なので値の代入はできない
# a[1] = 10
# print("a = {}".format(a))

e = ()
f = 10,
print("e = {}".format(e))
print("f = {}".format(f))
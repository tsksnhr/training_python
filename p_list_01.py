a = [1,2,3]
b = []
c = [99,101,102]

c.insert(0,98)
c.insert(2,100)
print(c)
print("---")

b.append(4)
b.append(5)

print(a)
print(b)
print("---")

# リストの足し算では元のリストの値は変更されない
print(a+b)
print(a)
print(b)
print("---")

# extendを使用すると元のリストの値も更新される
a.extend(b)
print(a)
print(b)
print("a = {}".format(a))

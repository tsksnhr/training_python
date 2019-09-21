# {}は空の辞書、空の集合を作成したい場合はset()を使う
s = set()
print(s)

s.add(1)
s.add(2)
s.add(3)
s.add(3)
print(s)

print(2 in s)
print(5 in s)

print("---")

p = {2,3,4}
print(p)

print("---")

print(s&p)
print(s|p)
print(s-p)

print("---")

for column in s|p:
    print(column)
d1 = {"a": 1, "b": 2, "c": 3}

print(d1["a"])
print(d1["b"])
print(d1["c"])

if "d" in d1 == True:
    print(d1["d"])
else:
    print("nothing")

print("---")

d2 = {}
d2["x"] = 10
d2["y"] = 20
d2["z"] = 30

print(d2)

for column in d2:
    print(column)

print("keys")
for key in d2.keys():
    print(key)

print("value")
for value in d2.values():
    print(value)

print("items")
for item in d2.items():
    print(item)
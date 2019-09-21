import json

data = {"a":1,
        "b":2,
        "c":[1,2,3],
        "d":{"a":1, "b":2}}

s = json.dumps(data)
print(s)

data2 = json.loads(s)
print(data2)
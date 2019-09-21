d = {"a":1, "b":2, "c":3}

"""
try:
    print(d["d"])
except KeyError as error:
    print("KeyError!: {}".format(error))
"""
"""
try:
    print(d["d"])
except:
    print("something is wrong")
"""

try:
    print(d["d"])
except Exception as error:
    print(type(error))
    print(error)
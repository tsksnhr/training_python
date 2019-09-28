# challenge 01
def square(x):
    return x**2

print(square(10))

# challenge 02
def printstring(x):
    str(x)
    print(x)

printstring(10)

# challenge 03
def hoge(x, y, z, i=1, j=11):

    ans = []

    if i == 1:
        for dummy in range(j):
            ans.append(x+y+z+dummy)

    else:
        for dummy in range(j):
            ans.append(x+y+dummy)

    return ans

print(hoge(1,2,3))
print(hoge(1,2,3,i=0))

# challenge 04
def stringtofloat(x):
    try:
        float(x)
        print(x)
    except(ValueError, NameError):
        print("Invalid attribute")

stringtofloat(10)
stringtofloat(2.5)
stringtofloat("abc")

# challenge 05
def hurfnum(x):
    return int(x/2)

def mul4(x):
    return x*4

print(mul4(hurfnum(10)))
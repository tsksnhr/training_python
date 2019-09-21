def f(a = 100, b = 10):
    return a**2 + 2*a*b + b

print( f(4,5) )
print( f(4) )
print( f(b = 25) )
print( f(100, 25) )
print( f(b = 25, a = 100))
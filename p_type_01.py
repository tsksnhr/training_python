string = "toshiki"
number_n = "123"
number_r = "45.6"

n = 5
r = 2.3
a = 8

r1 = 2.5
r2 = 4.7

print("---")
print(string)
print(string + str(n))
print(string + str(r))
print("---")

print("---")
print( int(number_n) + n )
# print( int(number_r)+r)
print( float(number_r)+r)
print("---")

print("---")
print(n+r)
print(str(n)+str(r))
print("---")

print("---")
print("sum of {} and {} is {}".format(n,a,n+a))
print("---")

print("---")
print("div of {} and {} is {:4.2f}".format(r1,r2,r2/r1))
print("---")
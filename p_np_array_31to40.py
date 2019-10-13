import numpy as np

# 31 How to ignore all numpy warnings (not recommended)? (★☆☆)

defaults = np.seterr(all = "ignore")
Z = np.array([[1,2],[3,4]])
#Z = Z/0
print(Z)

_ = np.seterr(**defaults)

# 32 Is the following expressions true? (★☆☆)
print(np.sqrt(-1) == np.emath.sqrt(-1))     # False

# 33 How to get the dates of yesterday, today and tomorrow? (★☆☆)
print(np.datetime64("today", "D") - np.timedelta64(1, "D"))
print(np.datetime64("today", "D"))
print(np.datetime64("today", "D") + np.timedelta64(1, "D"))

# 34 How to get all the dates corresponding to the month of July 2016? (★★☆)
A = np.arange('2016-07', "2016-08", dtype = "datetime64[D]")
print(A)

# 35 How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)
A = np.ones((3,3))
B = np.ones((3,3))*2
print(((A+B)*(-A/2)))
np.add(A,B, out = B)
np.divide(A,2, out = A)
np.negative(A, out = A)
print(np.multiply(A,B, out = A))

# 36 Extract the integer part of a random array using 5 different methods (★★☆)

# 37 Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)

# 38 Consider a generator function that generates 10 integers and use it to build an array (★☆☆)

# 39 Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)

# 40 Create a random vector of size 10 and sort it (★★☆)¶

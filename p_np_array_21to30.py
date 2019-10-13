import numpy as np

#21 Create a checkerboard 8x8 matrix using the tile function
A = np.array([0,1])
A = np.tile(A, (8,8))
print(A)

#22 Normalize a 5x5 random matrix
A = np.random.random((5,5))
print(A)
A = (A - np.mean(A))/np.std(A)
print(A)

#23 Create a custom dtype that describes a color as four unsigned bytes (RGBA)
A = np.dtype([("R", np.ubyte, 1),("G", np.ubyte, 1),("B", np.ubyte, 1), ("A", np.ubyte, 1)])
print(A)

#24 Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
A = np.random.random((5,3))
B = np.random.random((3,2))
print(A)
print(B)
print(np.dot(A,B))

#25 Given a 1D array, negate all elements which are between 3 and 8, in place
A = np.arange(11)
print(A)
A[(3<=A)&(A<=8)] *= -1
print(A)

#26  What is the output of the following script? 

print(sum(range(5),-1))     # 1+2+3+4-1
#from numpy import *
print(sum(range(5),-1))     # ???

#27 Consider an integer vector Z, which of these expressions are legal?

Z = np.arange(10)
print(Z**Z)             # square and cast
print(2 << Z >> 2)      # ?
print(Z <- Z)           # comparison each factor
print(1j*Z)             # imaginary factor
print(Z/1/1)            # not natural number
#print(Z<Z>Z)            # illegal

#28 What are the result of the following expressions?

print(np.array(0) / np.array(0))                        # 0 divide = nan
print(np.array(0) // np.array(0))                       # 
print(np.array([np.nan]).astype(int).astype(float))     # round to int,and cast to float

#29 How to round away from zero a float array ?

A = np.zeros((3,3))
print(A)
A = A.astype(float)
print(A)

# model answer
Z = np.random.uniform(-10,+10,10)
print(Z)
print (np.copysign(np.ceil(np.abs(Z)), Z))

#30 How to find common values between two arrays?
A = np.eye(3)
B = np.ones((3,3))
for i in range(3):
    for j in range(3):
        if A[i,j] == B[i,j]:
            print(True)
        else:
            print(False)

# model answer
A = np.eye(3)
B = np.ones((3,3))
print(np.intersect1d(A,B))

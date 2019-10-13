import numpy as np

#11 Create a 3x3 identity matrix
A = np.eye(3)
print(A)

#12 Create a 3x3x3 array with random values
# miss
# A = np.random.randint(1,9,27)
# A = A.reshape(3,3,3)
# print(A)

A = np.random.random((3, 3, 3))
print(A)

#13 Create a 10x10 array with random values and find the minimum and maximum values
# miss
# A = np.random.random((10,10))
# A = A[max(A) and min(A)]
# print(A)

A = np.random.random((10,10))
Amax, Amin = A.max(), A.min()
print(Amax, Amin)

#15  Create a random vector of size 30 and find the mean value
v_ = np.random.random(30)
v_mean = v_.mean()
print(v_mean)

#16 Create a 2d array with 1 on the border and 0 inside
# miss
# A = np.ones((3,3))
# A[1, 1] = 0
# print(A)

A = np.ones((10,10))
A[1:-1,1:-1] = 0
print(A)

#17 What is the result of the following expression?
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)

#18 Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
A = np.zeros((5,5))
for i in range(1,5):
    A[i,i-1] = i
print(A)

# model answer
Z = np.diag(1+np.arange(4),k=-1)
print(Z)

#19 Create a 8x8 matrix and fill it with a checkerboard pattern
A = np.zeros((8,8))
for i in range(0,8):
    if i%2 == 0:
        for j in range(0,7,2):
            A[i,j] = 1
    else:
        for k in range(1,9,2):
            A[i,k] = 1
print(A)

# model answer
Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)

#20 Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
A = np.arange(0,6*7*8)
A = A.reshape(6,7,8)
print(A)

# model answer
print(np.unravel_index(99,(6,7,8)))
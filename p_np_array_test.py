import numpy as np

# print(np.__version__)
# np.show_config()

print(np.zeros(10))

A = np.zeros(10)
print(A.size*A.itemsize)

A = np.zeros(10)
A[4] = 1
print(A)

A = np.arange(10,50)
print(A)

A = A[::-1]
print(A)

A = np.arange(0,9).reshape(3,3)
print(A)

A = [1,2,0,0,4,0]
B = np.nonzero(A)
print(B)

print(np.eye(3))

print(np.random.random((3,3,3)))

A = np.random.random((10,10))
A_max,A_min = A.max(), A.min()
print(A_max,A_min)

A = np.random.random(30)
A_mean = np.mean(A)
print(A_mean)

A = np.ones((5,5))
A[1:-1,1:-1] = 0
print(A)

A = np.ones((5,5))
A = np.pad(A, pad_width = 1, mode = 'constant', constant_values = 0)
print(A)

print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)

A = np.diag(1+np.arange(4), k = -1)
print(A)

A = np.zeros((8,8))
A[1::2,::2] = 1
A[::2,1::2] = 1
print(A)

A = np.arange(1,4)
B = np.arange(5,8)
C = np.c_[A,B]
print(A)
print(B)
print(C)
D = [1,2,3]
E = [5,6,7]
F =D+E
print(F)
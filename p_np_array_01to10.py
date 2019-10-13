#1 Import the numpy package under the name np
import numpy as np

#2 Print the numpy version and the configuration
print(np.__version__)
np.show_config()

#3 Create a null vector of size 10
z_ = np.zeros(10)
print(z_)

#4 How to find the memory size of any array
# miss
# A = np.arange(1,10)
# print(A)
# print(np.size(A))
A = np.zeros((10,10))
print("{} bites".format(A.size*A.itemsize))

#5 How to get the documentation of the numpy add function from the command line?
# %run 'python -c "import numpy; numpy.info(numpy.add)"'

#6 Create a null vector of size 10 but the fifth value which is 1
z_ = np.zeros(10)
z_[4] = 1
print(z_)

#7 Create a vector with values ranging from 10 to 49
v_ = np.arange(10,50)
print(v_)

#8 Reverse a vector (first element becomes last)
v_ = v_[::-1]
print(v_)

#9 Create a 3x3 matrix with values ranging from 0 to 8
A = np.arange(0,9).reshape(3,3)
print(A)

#10 Find indices of non-zero elements from [1,2,0,0,4,0]
A = np.array([1,2,0,0,4,0])
A = A[A != 0]
print(A)

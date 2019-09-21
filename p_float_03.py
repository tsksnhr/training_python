# 計算途中で数値が極端に大きくなる計算は、途中計算が変数型で扱えるようにすること
import numpy as np

def softplus(x):
    return np.log(1+np.exp(x))
"""
for i in range(-3,1000,1):
    print("i={}".format(i))
    print(softplus(i))
"""

def softplus_a(x):
    return max(0,x)+np.log(1+np.exp(-abs(x)))

for i in range(-3,1000,1):
    print("i={}".format(i))
    print(softplus_a(i))
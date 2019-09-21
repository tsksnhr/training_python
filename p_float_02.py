# 引き算の絶対値が小さくなるような計算は避ける！
import numpy as np

def qeq01(a, b, c):
    d = np.sqrt(b**2-4*a*c)
    answer01 = (-b+d)/(2*a)
    answer02 = (-b-d)/(2*a)
    return answer01, answer02

print(qeq01(1,5,6))
print(1.000000001**2-4*1*0.000000001)
print(qeq01(1, 1.000000001, 0.000000001))
print("---")

def qeq02(a,b,c):
    d = np.sqrt(b**2-4*a*c)
    answer01 = (-b-np.sign(b)*d)/(2*a)
    answer02 = c/(a*answer01)
    return answer01,answer02

print(qeq02(1,1.000000001,0.000000001))
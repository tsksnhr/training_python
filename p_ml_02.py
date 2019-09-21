import numpy as np
import matplotlib.pyplot as plt

def regl2dim(x, y):
    n = len(x)
#    a = ((1/n)*x.sum()*y.sum() - (x*y).sum())/((x**2).sum() - (1/n)*(x.sum())**2)      # Equation mistake
    a = (np.dot(x, y) - (1/n)*(x.sum()*y.sum()))/((x**2).sum() - (1/n)*(x.sum())**2)
#    a = ((x*y).sum() - (1/n)*(x.sum()*y.sum()))/((x**2).sum() - (1/n)*(x.sum())**2)
    b = (1/n)*((y - a*x).sum())
    return a, b

x = np.array([1, 2, 4, 6, 7])
y = np.array([1, 3, 3, 5, 4])
a, b = regl2dim(x, y)

plt.scatter(x, y, color = "k")
xmax = x.max()
plt.plot([0, xmax], [b, a*xmax + b], color = "k")

plt.show()

print((x*y).sum())
print(np.dot(x, y))

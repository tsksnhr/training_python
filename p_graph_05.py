import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

l = []
for n in range(1000):
    temp = np.random.randint(1, 7, size = 10)
    temp = temp.sum()
    l.append(temp)

plt.hist(l, 20, color = "gray")
plt.show()

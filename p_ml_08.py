import p_ml_06
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

x = np.array([1, 2, 4, 6, 7])
y = np.array([1, 3, 3, 5, 4])
model = p_ml_06.RidgeRegression()
model.fit(x, y)
b, a = model.w_


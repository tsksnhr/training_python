import numpy as np
import matplotlib.pyplot as plt

THRESHMIN = 1e-10

def sigmoid(x):
    return 1/(1 + np.exp(-x))

class LogisticRegression:
    def __init__(self, tol = 0.01, max_iter = 3, random_seed = 0):
        self.tol = tol
        self.max_iter = max_iter
        self.random_state = np.random.RandomState(random_seed)
        self.w_ = None

    def fit(self, X, y):
        self.w_ = self.random_state.randn(X.shape[1] + 1)
        Xtil = np.c_[np.ones(X.shape[0], X)]
        diff = np.inf
        w_prev = self.w_
        iter = 0
        while (diff > self.tol) and (iter < self.max_iter):
            yhat = sigmoid(np.dot(Xtil, self.w_))
            

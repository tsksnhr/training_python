import numpy as np

np.random.seed(10)
print(np.random.rand(5))

np.random.seed(10)
print(np.random.rand(5))

def dice_throw(n, seed):
    np.random.seed(seed)
    return (np.random.randint(1, 7, size = (n))).sum()

print(dice_throw(10, 2))
print(dice_throw(10, 2))

print(dice_throw(10, 4))
print(dice_throw(10, 4))
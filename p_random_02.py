import numpy as np

def dice_throw(n):
    return (np.random.randint(1, 7, size = n)).sum()

print(dice_throw(99))
import numpy as np

rs = np.random.RandomState(24)
print(rs)
print(rs.rand())

class Dice:
    def __init__(self, random_seed = None):
        self.random_state_ = np.random.RandomState(random_seed)
        self.sum_ = 0

    def throw(self):
        self.sum_ += self.random_state_.randint(1, 7)

    def get_sum(self):
        return self.sum_

d0 = Dice(24)
d1 = Dice(24)

for i in range(10):
    d0.throw()
    d1.throw()

print(d0.get_sum())
print(d1.get_sum())

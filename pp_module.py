# challenge 01

import statistics as stat
import random

rand_list = []

for dummy in range(10):
    rand_list.append(random.randint(1,100))

print(rand_list)
print(stat.mean(rand_list))
print(stat.median(rand_list))
print(stat.mode(rand_list))



# challenge 02

import pp_cubed as c

print(c.cubed(10))
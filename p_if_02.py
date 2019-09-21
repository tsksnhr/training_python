import random as random

number_list = [27,45,86,125,4]

x = random.choice(number_list)

print("random number is {}".format(x))

if x > 50:
    print("big!")
else:
    print("small!")
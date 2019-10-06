# challenge 01

class Square:

    square_list = []

    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.square_list.append((self.width, self.length))

test_0 = Square(5, 5)
test_1 = Square(10, 10)
test_2 = Square(15, 15)

print(Square.square_list)

#challenge 02

class Square_diff:

    def __init__(self, length):
        self.length = length

    def __repr__(self):
        return "{} by {} by {} by {}.".format(self.length, self.length, self.length, self.length)

print(Square_diff(29))

# challenge 03

def dit_obj(a, b):
    if a is b:
        return True
    else:
        return False

same_test = test_0

print(dit_obj(test_0, same_test))
print(test_0)
print(same_test)
print(dit_obj(test_0, test_1))
print(test_1)
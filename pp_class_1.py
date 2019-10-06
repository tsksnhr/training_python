# challenge 01
# challenge 02

"""
class Rectange:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calc_perimiter(self):
        return (self.width*2 + self.length*2)
"""
"""    
class Square:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calc_perimiter(self):
        return (self.width*2 + self.length*2)
"""
"""
class Square(Rectange):
    def change_size(self, variable):
        self.length += variable

test_0 = Rectange(10, 10)
test_1 = Square(10, 10)
print(test_0.calc_perimiter())
print(test_1.calc_perimiter())

test_1.change_size(-3)
print(test_1.calc_perimiter())
"""

# challenge 03

class Shape:
    def what_am_I(self):
        print("I am shape!")

class Rectange(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calc_perimiter(self):
        return (self.width*2 + self.length*2)

class Square(Rectange):
    pass

test_2 = Rectange(10, 5)
test_3 = Square(10, 5)

test_2.what_am_I()
test_3.what_am_I()

# challenge 04

class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

test_4 = Rider("Takeshi")
test_5 = Horse("hoge", test_4)
print(test_5.rider.name)

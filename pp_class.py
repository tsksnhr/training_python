import numpy as np

# challenge 01

class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    def area(self):
        return (self.diameter/2)**2*np.pi

test_0 = Circle(10)
print(test_0.area())

# challenge 02

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base*self.height)/2

test_1 = Triangle(10, 10)
print(test_1.area())

# challenge 03

class Hexagon:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def calc_perimeter(self):
        return self.base*6

test_02 = Hexagon(10, 10)
print(test_02.calc_perimeter())

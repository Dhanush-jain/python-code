import math

# Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
# Triangle class
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c
# Square class
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side
# Example usage
circle = Circle(5)
print("Circle - Area:", circle.area(), "Perimeter:", circle.perimeter())

triangle = Triangle(3, 4, 5)
print("Triangle - Area:", triangle.area(), "Perimeter:", triangle.perimeter())

square = Square(4)
print("Square - Area:", square.area(), "Perimeter:", square.perimeter())
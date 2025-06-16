from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod  
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    print(shape.area())
    print(shape.perimeter())

circle = Circle(radius=5)
shape_info(circle)

rectangle = Rectangle(4,8)
shape_info(rectangle)


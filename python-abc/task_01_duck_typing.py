from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod  
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

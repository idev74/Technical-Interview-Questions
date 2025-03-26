'''
Implement the Prototype design pattern.

The Prototype is a creational design pattern that allows an object to copy itself. It is particularly useful when the creation of an object is more convenient through copying an existing object than through creation from scratch.

Your are given a `Shape` prototype interface that supports cloning itself within the `Rectangle` and `Square` classes.

You need to implement the following:

The `clone()` method in the `Rectangle` class which returns a new instance of the `Rectangle` class.
The `clone()` method in the `Square` class which returns a new instance of the `Square` class.
The `cloneShapes()` method in the Test class which returns a list of cloned shapes.
'''

# Solution
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def clone(self):
        pass

class Square(Shape):
    def __init__(self, length: int):
        self.length = length

    def get_length(self) -> int:
        return self.length

    def clone(self) -> Shape:
        return Square(self.length)

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def clone(self) -> Shape:
        return Rectangle(self.width, self.height)

class Test:
    def clone_shapes(self, shapes: List[Shape]) -> List[Shape]:
        return [shape.clone() for shape in shapes]

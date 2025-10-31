import numpy as np
from shape import Shape
import utils as utl


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        utl.validate_positive_numbers(value)
        self._radius = value

    @property
    def perimeter(self) -> float:
        return 2 * np.pi * self.radius

    @property
    def area(self) -> float:
        return np.pi * self.radius**2

    def __repr__(self):
        return f"Circle (x={self.x}, y={self.y}, radius={self.radius}, circumference={self.perimeter}, area={self.area})"

    def __str__(self):
        return f"A circle that is located at (x = {self.x} y = {self.y}) it has a circumference of {self.perimeter} and an area of {self.area})"

    def is_unit_circle(self) -> bool:
        if self.x == 0 and self.y == 0 and self.radius == 1:
            return True
        else:
            return False

    def __eq__(self, other) -> bool:
        # I did google how to check if two circles are equal and took the formula but the code is all mine
        return (
            type(self) is type(other)
            and ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5 == 0
            and self.radius == other.radius
        )

    def __lt__(self, other) -> bool:
        return self.radius < other.radius

    def __le__(self, other) -> bool:
        return self.radius <= other.radius

    def __gt__(self, other) -> bool:
        return self.radius > other.radius

    def __ge__(self, other) -> bool:
        return self.radius >= other.radius

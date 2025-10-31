import numpy as np
from shape import Shape


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def circumference(self) -> float:
        return 2 * np.pi * self.radius

    @property
    def area(self) -> float:
        return np.pi * self.radius**2

    def __repr__(self):
        return f"Circle (x={self.x}, y={self.y}, radius={self.radius}, circumference={self.circumference}, area={self.area})"
    
    def __str__(self):
        return f"A circle that is located at (x = {self.x} y = {self.y}) it has a circumference of {self.circumference} and an area of {self.area})"

    def is_unit_circle(self) -> bool:
        if self.x == 0 and self.y == 0 and self.radius == 1:
            return True
        else:
            return False
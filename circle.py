import numpy as np
from shape import Shape
import utils as utl
from numbers import Number


class Circle(Shape):
    """
    A class representing a circle

    Attributes:
    - x (float): x position of the circle
    - y (float): y position of the circle
    - radius (float): radius of the circle
    - area (float): area of the circle
    - perimeter(float): perimeter of circle

    Nethods:
    - translate(x:float, y:float): adds the new x and y to the current position
    - is_unit_circle() -> bool: returns True if the circle is located at 0, 0 and has a radius of 1 otherwise False

    Example usage:
    >>> circle1 = circle(0,0,1)
    >>> circle1.is_unit_circle()
    True
    >>> circle1.translate(2,3)
    >>> print(circle1)
    A circle that is located at (x = 0 y = 0) it has a circumference of 12.566370614359172 and an area of 12.566370614359172)
    """
    def __init__(self, x :Number = 0, y :Number = 0, radius :Number = 1):
        """
        Initializes a new instance of the circle class.

        Parameters:
        - x (float): x position of the circle
        - y (float): y position of the circle
        - radius (float): radius of the circle
        """
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
        return f"Circle (x={self.x}, y={self.y}, radius={self.radius}, perimeter={self.perimeter}, area={self.area}"

    def __str__(self):
        return f"A circle that is located at (x = {self.x} y = {self.y}) it has a perimeter of {self.perimeter} and an area of {self.area})"

    def is_unit_circle(self) -> bool:
        """returns True if the circle is located at 0, 0 and has a radius of 1 otherwise False"""
        if self.x == 0 and self.y == 0 and self.radius == 1:
            return True
        else:
            return False


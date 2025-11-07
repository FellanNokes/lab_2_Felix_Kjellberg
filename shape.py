import utils as utl
from numbers import Number
class Shape():
    """
    A class representing a shape

    Attributes:
    - x (float): x position of the shape
    - y (float): y position of the shape

    Nethods:
    - translate(x:float, y:float): adds the new x and y to the current position

    Example usage:
    >>> shape1 = Shape(1,3)
    >>> shape1.translate(2,7)
    >>> print(shape1)
    A shape located at (x:3, y:10)
    """
    def __init__(self, x : Number= 0, y: Number = 0):
        """
        Initializes a new instance of the Shape class.

        Parameters:
        - x (float): x position of the shape
        - y (float): y position of the shape
        """
        utl.validate_numbers(x,y)
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def area(self):
        return 0
    
    def __repr__(self):
        return f"Shape(x = {self.x},y = {self.y})"
    
    def __str__(self):
        return f"A shape located at (x:{self.x}, y:{self.y})"

    def translate(self, x, y):
        """Adds a new position to the current position"""
        utl.validate_numbers(x,y)
        self._x += x
        self._y += y

    #TODO: maybe we want a reset position to 0, 0
    def __eq__(self, other) -> bool:
        return (
            type(self) is type(other)
            and self.area == other.area
        )

    def __lt__(self, other) -> bool:
        return self.area < other.area

    def __le__(self, other) -> bool:
        return self.area <= other.area

    def __gt__(self, other) -> bool:
        return self.area > other.area

    def __ge__(self, other) -> bool:
        return self.area >= other.area
    
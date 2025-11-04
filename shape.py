import utils as utl
class Shape():
    """
    A class representing a shape

    Attributes:
    - x (float): x position of the shape
    - y (float): y position of the shape

    Nethods:
    - translate(): adds the new x and y to the current position

    Example usage:
    >>> shape1 = Shape(1,3)
    >>> shape1.translate(2,7)
    >>> print(shape1)
    A shape located at (x:3, y:10)
    """
    def __init__(self, x, y):
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
    
    def __repr__(self):
        return f"Shape(x = {self.x},y = {self.y})"
    
    def __str__(self):
        return f"A shape located at (x:{self.x}, y:{self.y})"

    #TODO: add validation 
    def translate(self, x, y):
        """Adds a new position to the current position"""
        utl.validate_numbers(x,y)
        self._x += x
        self._y += y

    #TODO: maybe we want a reset position to 0, 0
    
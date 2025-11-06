import utils as utl
from shape import Shape
from numbers import Number

class Cube(Shape):
    """
    A class representing a cube

    Attributes:
    - x (float): x position of the cube
    - y (float): y position of the cube
    - size (float): sidelenght of the cube
    - area (float): the surface area of the cube
    - sidearea(float): sidearea of one side of the cube
    - volume(float): the volume of the cube

    Nethods:
    - translate(x:float, y:float): adds the new x and y to the current position

    Example usage:
    >>> cube1 = cube(0,0,10)
    >>> cube1.translate(2,3)
    >>> print(cube1)
    A cube located at (x = 2, y 3) it has the surface area of 600 and the volume of 1000
    """
    def __init__(self, x: Number = 0, y: Number = 0, size: Number = 1):
        """
        Initializes a new instance of the Cube class

        Parameters:
        - x (float): x position of the cube
        - y (float): y position of the cube
        - size (float): the length of each side of the cube
        """
        super().__init__(x, y)
        self.size = size

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        utl.validate_positive_numbers(value)
        self._size = value
    
    @property
    def sidearea(self) -> float:
        return self.size**2
    
    @property
    def area(self) -> float:
        """Returns the surface area of a cube"""
        return self.sidearea * 6
    
    @property
    def volume(self) -> float:
        return self.size ** 3
    
    def __repr__(self):
        return f"Cube (x ={self.x},y ={self.y}, size={self.size}, volume={self.volume}, sidearea={self.sidearea}, area={self.area})"

    def __str__(self):
        return f"A cube located at (x = {self.x}, y {self.y}) each side is {self.size} long it has the surface area of {self.area} and the volume of {self.volume}"
    

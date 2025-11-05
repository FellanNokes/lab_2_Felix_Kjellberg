import utils as utl
from shape import Shape

class Cube(Shape):
    """
    A class representing a cube

    Attributes:
    - x (float): x position of the cube
    - y (float): y position of the cube
    - sidelength (float): sidelenght of the cube
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
    def __init__(self, x, y, sidelength: float):
        """
        Initializes a new instance of the Cube class

        Parameters:
        - x (float): x position of the cube
        - y (float): y position of the cube
        - sidelength (float): the length of side of the cube
        """
        super().__init__(x, y)
        self.sidelength = sidelength

    @property
    def sidelength(self):
        return self._sidelength
    
    @sidelength.setter
    def sidelength(self, value):
        utl.validate_positive_numbers(value)
        self._sidelength = value
    
    @property
    def sidearea(self) -> float:
        return self.sidelength**2
    
    @property
    def area(self) -> float:
        """Returns the surface area of a cube"""
        return self.sidearea * 6
    
    @property
    def volume(self) -> float:
        return self.sidelength ** 3
    
    def __repr__(self):
        return f"Cube (x ={self.x},y ={self.y}, sidelength={self.sidelength}, volume={self.volume}, sidearea={self.sidearea}, area={self.area})"

    def __str__(self):
        return f"A cube located at (x = {self.x}, y {self.y}) it has the surface area of {self.area} and the volume of {self.volume}"

    def __eq__(self, other) -> bool:
        return (
            type(self) is type(other)
            and ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5 == 0 #TODO: maybe just use other.x == self.x
            and self.volume == other.volume
        )

    def __lt__(self, other) -> bool:
        return self.volume < other.volume

    def __le__(self, other) -> bool:
        return self.volume <= other.volume

    def __gt__(self, other) -> bool:
        return self.volume > other.volume

    def __ge__(self, other) -> bool:
        return self.volume >= other.volume
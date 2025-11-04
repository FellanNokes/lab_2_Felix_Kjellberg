import utils as utl
from shape import Shape


class Rectangle(Shape):
    """
    A class representing a rectangle

    Attributes:
    - x (float): x position of the rectangle
    - y (float): y position of the rectangle
    - height (float): height of the rectangle
    - width (float): width of the rectangle
    - area (float): area of the rectanlge
    - perimeter(float): perimeter of rectangle

    Nethods:
    - translate(): adds the new x and y to the current position
    - is_square() -> bool: returns True if height and width are the same otherwise False

    Example usage:
    >>> rectangle1 = Rectangle(0,0,4,4)
    >>> rectangle1.is_square()
    True
    >>> rectangle1.translate(2,3)
    >>> print(rectangle1)
    A rectangle located at (x = 2, y = 3) it has a perimeter of 16 and an area of 16
    """
    def __init__(self, x: float, y: float, height: float, width: float):
        """
        Initializes a new instance of the Rectangle class.

        Parameters:
        - x (float): x position of the rectangle
        - y (float): y position of the rectangle
        - height (float): height of the rectangle
        - width (float): width of the rectangle
        """
        super().__init__(x, y)
        self.height = height
        self.width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        utl.validate_positive_numbers(value)
        self._height = value

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value):
        utl.validate_positive_numbers(value)
        self._width = value

    @property
    def area(self) -> float:
        return self.height * self.width

    @property
    def perimeter(self) -> float:
        return 2 * (self.height + self.width)
    
    def __repr__(self):
        return f"Rectangle (x ={self.x},y ={self.y}, height={self.height} width={self.width}, perimeter={self.perimeter}, area={self.area})"

    def __str__(self):
        return f"A rectangle located at (x = {self.x}, y = {self.y}) it has a perimeter of {self.perimeter} and an area of {self.area}"


    def is_square(self) -> bool:
        """returns True if height and width are the same otherwise False"""
        return self.width == self.height

    def __eq__(self, other) -> bool:
        return (
            type(self) is type(other)
            and ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5 == 0 #TODO: maybe just use other.x == self.x
            and self.height == other.height
            and self.width == other.width
        )

    def __lt__(self, other) -> bool:
        return self.area < other.area

    def __le__(self, other) -> bool:
        return self.area <= other.area

    def __gt__(self, other) -> bool:
        return self.area > other.area

    def __ge__(self, other) -> bool:
        return self.area >= other.area

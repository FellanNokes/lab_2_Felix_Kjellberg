import utils as utl
from shape import Shape


class Rectangle(Shape):
    def __init__(self, x: float, y: float, height: float, width: float):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def __repr__(self):
        return f"Rectangle (x ={self.x},y ={self.y}, height={self.height} width={self.width}, perimeter={self.perimeter}, area={self.area})"

    def __str__(self):
        return f"A rectangle located at (x = s{self.x}, y {self.y}) it has a perimeter of {self.perimeter} and an area of {self.area}"

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        utl.validate_positive_numbers(value)
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        utl.validate_positive_numbers(value)
        self._width = value

    @property
    def area(self) -> float:
        return self._height * self._width

    @property
    def perimeter(self) -> float:
        return 2 * (self._height + self._width)

    def is_square(self) -> bool:
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

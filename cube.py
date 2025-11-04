import utils as utl
from shape import Shape

class Cube(Shape):
    def __init__(self, x, y, sidelength: float):
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
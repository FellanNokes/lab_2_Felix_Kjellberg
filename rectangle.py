class Rectangle:
    def __init__(self, x: float, y: float, height: float, width: float):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def __repr__(self):
        return f"Rectangle with position x = {self.x},y = {self.y}, height = {self.height} width = {self.width}"
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def area(self):
        return self._height * self._width
    
    @property
    def perimeter(self):
        return 2 * (self._height + self._width)
    
    def is_square(self) -> bool:
        return self.width == self.height
    
    def __eq__(self, other) -> bool:
        return self.area == other.area
class Rectangle:
    def __init__(self, position: tuple, height: float, width: float):
        self.position = position
        self.height = height
        self.width = width
    
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


    

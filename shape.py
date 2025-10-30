import utils as utl
class Shape():
    def __init__(self, x, y):
        utl.validate_numbers(x,y)
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def translate(self, x, y):
        self._x += x
        self._y += y

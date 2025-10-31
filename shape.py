import utils as utl
#TODO: maybe we add operators here to be able to compare different shapes
#TODO: Add dunder repr and str
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

    #TODO: add validation 
    def translate(self, x, y):
        self._x += x
        self._y += y

    #TODO: maybe we want a reset position to 0, 0
    
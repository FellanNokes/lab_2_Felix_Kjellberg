import numpy as np

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value
    
    @property
    def circumference(self) -> float:
        return 2*(self.radius*np.pi)
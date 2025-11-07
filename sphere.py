from circle import Circle
import numpy as np
from numbers import Number
import utils as utl

class Sphere(Circle):
    """
    A class representing a sphere

    Attributes:
    - x (float): x position of the sphere
    - y (float): y position of the sphere
    - radius (float): radius of the sphere
    - area (float): the surface area of the sphere
    - sidearea(float): sidearea of one side of the sphere
    - volume(float): the volume of the sphere

    Nethods:
    - translate(x:float, y:float): adds the new x and y to the current position

    Example usage:
    >>> sphere1 = sphere(0,0,10)
    >>> sphere1.translate(2,3)
    >>> print(sphere1)
    a sphere located at (x:2, y:3) that has a radius of 10 it has a surface area of 1256.6370614359173 and a volume of 4188.790204786391
    """
    def __init__(self, x: Number = 0, y: Number = 0, z: Number = 0, radius: Number = 1):
        """
        Initializes a new instance of the sphere class.

        Parameters:
        - x (float): x position of the sphere
        - y (float): y position of the sphere
        - radius (float): radius of the sphere
        """
        super().__init__(x, y, radius)
        self._z = z

    @property
    def z(self) -> float:
        return self._z
    @property
    def volume(self) -> float:
        return 4/3 * np.pi * self.radius**3
    
    @property
    def area(self) -> float:
        return 4 * np.pi * self.radius**2
    
    def __repr__(self):
        return f"Sphere(x = {self.x}, y = {self.y}, z = {self.z}, radius = {self.radius}, volume = {self.volume}, area = {self.area})"
    
    def __str__(self):
        return f"a sphere located at (x:{self.x}, y:{self.y}, z:{self.z}) that has a radius of {self.radius} it has a surface area of {self.area} and a volume of {self.volume}"
    
    def translate(self, x, y, z):
        """Adds a new position to the current position"""
        utl.validate_numbers(x,y,z)
        self._x += x
        self._y += y
        self._z += z

    def is_unit_circle(self) -> None:
        NotImplemented
    
    def is_unit_sphere(self) -> bool:
        return self.x == 0 and self.y == 0 and self.z == 0 and self.radius == 1
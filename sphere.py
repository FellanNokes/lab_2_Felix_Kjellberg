from circle import Circle
import numpy as np

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
    def __init__(self, x, y, radius):
        """
        Initializes a new instance of the sphere class.

        Parameters:
        - x (float): x position of the sphere
        - y (float): y position of the sphere
        - radius (float): radius of the sphere
        """
        super().__init__(x, y, radius)

    @property
    def volume(self) -> float:
        return 4/3 * np.pi * self.radius**3
    
    @property
    def area(self) -> float:
        return 4 * np.pi * self.radius**2
    
    def __repr__(self):
        return f"Sphere(x = {self.x}, y = {self.y} radius = {self.radius})"
    
    def __str__(self):
        return f"a sphere located at (x:{self.x}, y:{self.y}) that has a radius of {self.radius} it has a surface area of {self.area} and a volume of {self.volume}"
    
    def is_unit_sphere(self):
        return self.x == 0 and self.y == 0 and self.radius == 1
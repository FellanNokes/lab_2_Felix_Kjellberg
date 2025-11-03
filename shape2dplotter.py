from rectangle import Rectangle
from circle import Circle
from shape import Shape
import matplotlib.patches as patches
import matplotlib.pyplot as plt


def plot_rectangle(rectangle: Rectangle):
    x = rectangle.x - rectangle.width*.5
    y = rectangle.y - rectangle.height*.5
    return patches.Rectangle([x,y], rectangle.width, rectangle.height, fc='none', ec ='r', lw= 2)
def plot_circle(circle: Circle):
    return patches.Circle([circle.x,circle.y], circle.radius, fc='none', ec ='b', lw= 2)
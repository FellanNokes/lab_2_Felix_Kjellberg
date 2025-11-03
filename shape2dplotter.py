from rectangle import Rectangle
from circle import Circle
from shape import Shape
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

class Shape2dPlotter:
    def __init__(self, *shapes: Shape):
        self._shapes = tuple(shapes)
        
    
    def plot(self, size):
        # I did first find this code here: https://pygmalion.nitri.org/cartesian-coordinates-with-matplotlib-1263.html 
        # I have made some changes by my self and with the help of ChatGPT
        fig, ax = plt.subplots(figsize=(20, 20))
        fig.patch.set_facecolor('#ffffff')

        #sets the length of y and x to all be the same as size
        ax.set(xlim=(-size, size), ylim=(-size, size), aspect='equal')

        # Removes the top and right spine and moves the bottom and the left spine to the center
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # places y in the top of the y axis and x to the right of x axis
        ax.set_xlabel('$x$', size=14, labelpad=-24, x=1.02)
        ax.set_ylabel('$y$', size=14, labelpad=-21, y=1.02, rotation=0)

        # sets the ticks so we get 1, 2 ,3 etc also removes the zero from y to make it look cleaner
        ticks = np.arange(-size, size + 1, 1)
        ax.set_xticks(ticks)
        ax.set_yticks(ticks[ticks != 0])

        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

        # Draw shapes
        for shape in self._shapes:
            if isinstance(shape, Circle):
                ax.add_patch(patches.Circle((shape.x, shape.y), shape.radius, fc='none', ec='b', lw=2))
            elif isinstance(shape, Rectangle):
                x = shape.x - shape.width * 0.5
                y = shape.y - shape.height * 0.5
                ax.add_patch(patches.Rectangle((x, y), shape.width, shape.height, fc='none', ec='r', lw=2))

        plt.show()
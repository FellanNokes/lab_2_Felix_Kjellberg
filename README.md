# Lab 2 – Felix Kjellberg

The purpose of this lab is to practice **object-oriented programming (OOP)** in Python, focusing on creating modular, reusable, and well-structured programs. Below, I explain my work and thought process throughout the lab.

---

## Table of Contents

* [UML](#uml)
* [Shapes](#shapes)
* [Plotter](#plotter)
* [Tests](#tests)

---

## UML

![UML2](UML/UML2.png)

This is the final UML draft I used after completing Task 1. It helped me determine where to start with my code and what needed to be included in each class.

---

## Shapes

I aimed to create modular code following the **DRY principle**. I started with a base `Shape` class that only stores `x` and `y` positions.

From there, I built `Circle` and `Rectangle` classes with their respective attributes. During this process, I realized that **comparison operators** would be useful in the `Shape` class.

For 3D shapes:

* `Sphere` inherits from `Circle`.
* `Cube` does **not** inherit from `Rectangle` because all sides of a cube are equal.
* Both **3D** classes have a **z** positional parameter aswell and overides the `translate()` method from shape

**Example usage:**

```python
circle = Circle(x=5, y=5, radius=3)
rectangle = Rectangle(x=2, y=3, width=4, height=6)
sphere = Sphere(x=1, y=2, z=3, radius=5)
cube = Cube(x=0, y=0, z=3, size=3)
```

---

## Plotter

The `Plotter` class took the most time to implement. My goal was to create a Cartesian graph with equal height and width. I used this code for the cartesian graph [this example](https://pygmalion.nitri.org/cartesian-coordinates-with-matplotlib-1263.html), but I:

* Cleaned up the code for clarity
* Added an option to call `plot()` during initialization
* Implemented **auto-sizing**: the plot checks all shapes to ensure none are out of bounds
* Implemented the actual plotting of the different shapes


Users can choose to enable or disable the auto-size and auto-plot feature.

**Example usage:**

```python
shapes = [circle, rectangle, sphere, cube]
plotter = Plotter(shapes=shapes, auto_size=True, auto_plot=True)

plotter = Plotter(shapes=shapes, auto_size=False, auto_plot=False)
plotter.plot(size=20)
```

---

## Tests

I wrote both **unit tests** and **manual tests** to verify that everything works as intended. While there is always room for more tests, I am satisfied with the coverage I achieved in this lab. In future projects, I plan to dedicate more time to creating comprehensive unit tests.

---

## Video
[link](https://youtu.be/-4R1mBkLU8Q)

---

This README provides a clear explanation of my workflow, decisions, and examples of how to use the classes developed in Lab 2.


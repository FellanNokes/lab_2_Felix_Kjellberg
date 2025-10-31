from pytest import raises
from rectangle import Rectangle

def test_init_x_y_valid():
    rectangle = Rectangle(2,-3 , 4, 5)
    assert rectangle.x == 2, rectangle.y == -3

def test_init_height_width_valid():
    rectangle = Rectangle(0,0,height= 4,width= 5)
    assert rectangle.height == 4, rectangle.width == 5

def test_negative_height_fail():
    with raises(ValueError):
        Rectangle(0,0,-4,1)

def test_negative_width_fail():
    with raises(ValueError):
        Rectangle(0,0,3,-1)

def test_zero_height_fail():
    with raises(ValueError):
        Rectangle(0,0,0,1)

def test_zero_width_fail():
    with raises(ValueError):
        Rectangle(0,0,3,0)

def test_area_valid():
    rectangle = Rectangle(0,0,2,2)
    assert rectangle.area == 4

def test_eq_same_values_valid():
    rect1 = Rectangle(0,1,2,2)
    rect2 = Rectangle(0,1,2,2)
    assert rect1 == rect2

def test_eq_different_values_not_same_valid():
    rect1 = Rectangle(0,1,2,2)
    rect2 = Rectangle(0,1,3,2)
    assert rect1 != rect2

def test_lt_different_values_valid():
    rect1 = Rectangle(0,1,2,2)
    rect2 = Rectangle(0,1,3,2)
    assert rect1 < rect2

def test_le_same_values_valid():
    rect1 = Rectangle(0,1,2,2)
    rect2 = Rectangle(0,1,2,2)
    assert rect1 <= rect2

def test_le_different_values_valid():
    rect1 = Rectangle(0,1,2,2)
    rect2 = Rectangle(0,1,3,2)
    assert rect1 < rect2

def test_gt_different_values_valid():
    rect1 = Rectangle(0,1,5,2)
    rect2 = Rectangle(0,1,3,2)
    assert rect1 > rect2

def test_ge_same_values_valid():
    rect1 = Rectangle(0,1,2,2)
    rect2 = Rectangle(0,1,2,2)
    assert rect1 >= rect2

def test_ge_different_values_valid():
    rect1 = Rectangle(0,1,4,2)
    rect2 = Rectangle(0,1,3,2)
    assert rect1 > rect2

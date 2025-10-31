from pytest import raises
from circle import Circle

def test_init_x_y_valid():
    circle = Circle(2,-3 , 4)
    assert circle.x == 2, circle.y == -3

def test_init_radius_valid():
    circle = Circle(1, 2, 6)
    assert circle.radius == 6

def test_init_negative_radius_fail():
    with raises(ValueError):
        Circle(1,1,-2)

def test_init_radius_str_fail():
    with raises(TypeError):
        Circle(1,4,"2")

def test_zero_radius_fail():
    with raises(ValueError):
        Circle(0,2,0)

def test_eq_same_radius_xy_valid():
    circle1 = Circle(4,4,4)
    circle2 = Circle(4,4,4)
    assert circle1 == circle2

def test_eq_same_radius_different_pos_not_same_valid():
    circle1 = Circle(3,4,4)
    circle2 = Circle(4,4,4)
    assert circle1 != circle2

def test_eq_same_pos_different_radius_not_same_valid():
    circle1 = Circle(4,4,1)
    circle2 = Circle(4,4,4)
    assert circle1 != circle2

def test_lt_different_values_valid():
    circle1 = Circle(0,1,2)
    circle2 = Circle(0,1,3)
    assert circle1 < circle2

def test_le_same_values_valid():
    circle1 = Circle(0,1,2)
    circle2 = Circle(0,1,2)
    assert circle1 <= circle2

def test_le_different_values_valid():
    circle1 = Circle(0,1,2)
    circle2 = Circle(0,1,3)
    assert circle1 < circle2

def test_gt_different_values_valid():
    circle1 = Circle(0,1,5)
    circle2 = Circle(0,1,3)
    assert circle1 > circle2

def test_ge_same_values_valid():
    circle1 = Circle(0,1,2)
    circle2 = Circle(0,1,2)
    assert circle1 >= circle2

def test_ge_different_values_valid():
    circle1 = Circle(0,1,4)
    circle2 = Circle(0,1,3)
    assert circle1 > circle2
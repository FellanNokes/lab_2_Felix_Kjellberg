from pytest import raises
from shape import Shape
from circle import Circle
from rectangle import Rectangle

def test_shape_values_valid():
    shape1 = Shape(4,6)
    assert shape1.x == 4 , shape1.y == 6

def test_shape_type_str_fail():
    with raises(TypeError):
        Shape("2",1)

def test_shape_translate_type_str_fail():
    with raises(TypeError):
        shape=Shape(2,3)
        shape.translate("2",3)

def test_shape_translate_valid():
    shape1 = Shape(4,6)
    shape1.translate(2,0)
    assert shape1.x == 6, shape1.y == 6

def test_different_shapes_eq_false():
    circle = Circle(0,0,1)
    rectangle = Rectangle (0,0,1,1)
    result = circle == rectangle
    assert result == False

def test_different_shape_lt_true():
    circle = Circle(0,0,1)
    rectangle = Rectangle (0,0,5,2)
    result = circle < rectangle
    assert result == True

def test_different_shape_lt_false():
    circle = Circle(0,0,10)
    rectangle = Rectangle (0,0,2,2)
    result = circle < rectangle
    assert result == False

def test_different_shape_le_true():
    circle = Circle(0,0,1)
    rectangle = Rectangle (0,0,5,2)
    result = circle <= rectangle
    assert result == True

def test_different_shape_le_false():
    circle = Circle(0,0,10)
    rectangle = Rectangle (0,0,2,2)
    result = circle <= rectangle
    assert result == False

def test_different_shape_gt_true():
    circle = Circle(0,0,10)
    rectangle = Rectangle (0,0,2,2)
    result = circle > rectangle
    assert result == True

def test_different_shape_gt_False():
    circle = Circle(0,0,1)
    rectangle = Rectangle (0,0,5,2)
    result = circle > rectangle
    assert result == False

def test_different_shape_ge_true():
    circle = Circle(0,0,10)
    rectangle = Rectangle (0,0,2,2)
    result = circle >= rectangle
    assert result == True

def test_different_shape_ge_False():
    circle = Circle(0,0,1)
    rectangle = Rectangle (0,0,5,2)
    result = circle >= rectangle
    assert result == False
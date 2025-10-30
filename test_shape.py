from pytest import raises
from shape import Shape

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

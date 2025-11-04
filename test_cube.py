from pytest import raises
from cube import Cube

def test_init_x_y_valid():
    cube = Cube(-2,-4, 4)
    assert cube.x == -2, cube.y == -4

def test_init_sidelength_valid():
    cube = Cube(2,3,5)
    assert cube.sidelength == 5

def test_negative_sidelength_fail():
    with raises(ValueError):
        Cube(2,3,-4)

def test_zero_sidelength_fail():
    with raises(ValueError):
        Cube(2,3,0)

def test_sidearea_valid():
    cube = Cube(1,6,4)
    assert cube.sidearea == 16

def test_area_valid():
    cube = Cube(1,6,4)
    assert cube.area == 96

def test_volume_valid():
    cube = Cube(1,6,4)
    assert cube.volume == 64

def test_eq_same_values_valid():
    cube1 = Cube(0,1,2)
    cube2 = Cube(0,1,2)
    assert cube1 == cube2

def test_eq_same_sidelengths_different_pos_not_same_valid():
    cube1 = Cube(3,4,4)
    cube2 = Cube(4,4,4)
    assert cube1 != cube2

def test_eq_same_pos_different_sidelengths_not_same_valid():
    cube1 = Cube(4,4,1)
    cube2 = Cube(4,4,4)
    assert cube1 != cube2

def test_lt_different_values_valid():
    cube1 = Cube(0,1,2)
    cube2 = Cube(0,1,3)
    assert cube1 < cube2

def test_le_same_values_valid():
    cube1 = Cube(0,1,2)
    cube2 = Cube(0,1,2)
    assert cube1 <= cube2

def test_le_different_values_valid():
    cube1 = Cube(0,1,2)
    cube2 = Cube(0,1,3)
    assert cube1 < cube2

def test_gt_different_values_valid():
    cube1 = Cube(0,1,5)
    cube2 = Cube(0,1,3)
    assert cube1 > cube2

def test_ge_same_values_valid():
    cube1 = Cube(0,1,2)
    cube2 = Cube(0,1,2)
    assert cube1 >= cube2

def test_ge_different_values_valid():
    cube1 = Cube(0,1,4)
    cube2 = Cube(0,1,3)
    assert cube1 > cube2
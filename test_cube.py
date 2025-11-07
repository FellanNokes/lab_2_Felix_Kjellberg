from pytest import raises
from cube import Cube

def test_init_x_y_valid():
    cube = Cube(-2,-4, 4, 4)
    assert cube.x == -2, cube.y == -4
    assert cube.z == 4

def test_init_size_valid():
    cube = Cube(2,3,1,5)
    assert cube.size == 5

def test_negative_size_fail():
    with raises(ValueError):
        Cube(2,3,1,-4)

def test_is_unit_cube_true():
    cube = Cube(0,0,0,1)
    assert cube.is_unit_cube() == True

def test_is_unit_cube_wrong_value_size_false():
    cube = Cube(0,0,0,1.5)
    assert cube.is_unit_cube() == False

def test_is_unit_cube_wrong_value_x_false():
    cube = Cube(1,0,0,1)
    assert cube.is_unit_cube() == False

def test_is_unit_cube_wrong_value_y_false():
    cube = Cube(0,-2,0,1)
    assert cube.is_unit_cube() == False

def test_is_unit_cube_wrong_value_z_false():
    cube = Cube(0,0,10,1)
    assert cube.is_unit_cube() == False

def test_zero_size_fail():
    with raises(ValueError):
        Cube(2,3,4,0)

def test_sidearea_valid():
    cube = Cube(1,6,4,4)
    assert cube.sidearea == 16

def test_area_valid():
    cube = Cube(1,6,2,4)
    assert cube.area == 96

def test_volume_valid():
    cube = Cube(1,6,3,4)
    assert cube.volume == 64

def test_eq_same_values_valid():
    cube1 = Cube(0,1,3,2)
    cube2 = Cube(0,1,3,2)
    assert cube1 == cube2

def test_eq_same_pos_different_sizes_not_same_valid():
    cube1 = Cube(4,4,4,1)
    cube2 = Cube(4,4,4,4)
    assert cube1 != cube2

def test_lt_different_values_valid():
    cube1 = Cube(0,1,4,2)
    cube2 = Cube(0,1,4,3)
    assert cube1 < cube2

def test_le_same_values_valid():
    cube1 = Cube(0,1,3,2)
    cube2 = Cube(0,1,3,2)
    assert cube1 <= cube2

def test_le_different_values_valid():
    cube1 = Cube(0,1,3,2)
    cube2 = Cube(0,1,3,3)
    assert cube1 < cube2

def test_gt_different_values_valid():
    cube1 = Cube(0,1,2,5)
    cube2 = Cube(0,1,2,3)
    assert cube1 > cube2

def test_ge_same_values_valid():
    cube1 = Cube(0,1,3,2)
    cube2 = Cube(0,1,3,2)
    assert cube1 >= cube2

def test_ge_different_values_valid():
    cube1 = Cube(0,1,1,4)
    cube2 = Cube(0,1,1,3)
    assert cube1 > cube2
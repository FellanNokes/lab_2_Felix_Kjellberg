from pytest import raises
from sphere import Sphere

def test_init_x_y_z_valid():
    sphere = Sphere(2,-3, 2, 4)
    assert sphere.x == 2, sphere.y == -3
    assert sphere.z == 2

def test_init_radius_valid():
    sphere = Sphere(1, 2, 3, 6)
    assert sphere.radius == 6

def test_area_valid():
    sphere = Sphere(2,3, 2, 10)
    assert round(sphere.area, 3) == 1256.637

def test_volume_valid():
    sphere = Sphere(2,3,4,10)
    assert round(sphere.volume, 3) == 4188.790

def test_init_negative_radius_fail():
    with raises(ValueError):
        Sphere(1,1,1,-2)

def test_init_radius_str_fail():
    with raises(TypeError):
        Sphere(1,4,1,"2")

def test_zero_radius_fail():
    with raises(ValueError):
        Sphere(0,2,1,0)

def test_is_unit_sphere_true():
    sphere = Sphere(0,0,0,1)
    assert sphere.is_unit_sphere() == True

def test_is_unit_sphere_wrong_value_radius_false():
    sphere = Sphere(0,0,0,1.5)
    assert sphere.is_unit_sphere() == False

def test_is_unit_sphere_wrong_value_x_false():
    sphere = Sphere(1,0,0,1)
    assert sphere.is_unit_sphere() == False

def test_is_unit_sphere_wrong_value_y_false():
    sphere = Sphere(0,-2,0,1)
    assert sphere.is_unit_sphere() == False

def test_is_unit_sphere_wrong_value_z_false():
    sphere = Sphere(0,0,10,1)
    assert sphere.is_unit_sphere() == False


def test_eq_same_radius_xy_valid():
    sphere1 = Sphere(4,4,1,4)
    sphere2 = Sphere(4,4,1,4)
    assert sphere1 == sphere2

def test_eq_same_pos_different_radius_not_same_valid():
    sphere1 = Sphere(4,4,4,1)
    sphere2 = Sphere(4,4,4,4)
    assert sphere1 != sphere2

def test_lt_different_values_valid():
    sphere1 = Sphere(0,1,3,2)
    sphere2 = Sphere(0,1,3,3)
    assert sphere1 < sphere2

def test_le_same_values_valid():
    sphere1 = Sphere(0,1,2,2)
    sphere2 = Sphere(0,1,2,2)
    assert sphere1 <= sphere2

def test_le_different_values_valid():
    sphere1 = Sphere(0,1,2,2)
    sphere2 = Sphere(0,1,2,3)
    assert sphere1 < sphere2

def test_gt_different_values_valid():
    sphere1 = Sphere(0,1,2,5)
    sphere2 = Sphere(0,1,2,3)
    assert sphere1 > sphere2

def test_ge_same_values_valid():
    sphere1 = Sphere(0,1,2,2)
    sphere2 = Sphere(0,1,2,2)
    assert sphere1 >= sphere2

def test_ge_different_values_valid():
    sphere1 = Sphere(0,1,2,4)
    sphere2 = Sphere(0,1,2,3)
    assert sphere1 > sphere2
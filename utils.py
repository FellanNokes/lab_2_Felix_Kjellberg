from numbers import Number
import numpy as np

def validate_numbers(*values):
    for value in values:
        if not isinstance(value, Number):
                    raise TypeError(f"value must be number not {type(value)}")

def validate_positive_numbers(*values) -> None:
        for value in values:
            validate_numbers(value)
            if value <= 0:
                raise ValueError(f"Value can't be negative, not {value}")
            
def add_to_max(a, b, value):
      return np.maximum(a,b) + value

def validate_type(*values, type_value: type) -> None:
    for value in values:
        if not isinstance(value, type_value):
            raise ValueError(
                f"{value!r} must be of type {type_value.__name__}, not {type(value).__name__}"
            )
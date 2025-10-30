from numbers import Number

def validate_numbers(*values):
    for value in values:
        if not isinstance(value, Number):
                    raise TypeError(f"value must be number not {type(value)}")

def validate_positive_numbers(*values) -> None:
        for value in values:
            validate_numbers(value)
            if value < 0:
                raise ValueError(f"Value can't be negative, not {value}")
            

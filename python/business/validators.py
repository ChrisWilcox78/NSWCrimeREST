from functools import wraps


def provided(*param_names):
    """
    Validates that the specified parameters have been provided.
    """
    def validate_provided(*args, **kwargs):
        for param in param_names:
            if param in kwargs.keys() and kwargs[param] is None:
                raise ValueError("{} must be provided".format(param))
    return validate_provided


def validate_before(*validators):
    """
    A decorator that applies the specified validators before executing the decorated function/method.
    """
    def validation_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for validator in validators:
                validator(*args, **kwargs)
            return fn(*args, **kwargs)
        return wrapper
    return validation_decorator

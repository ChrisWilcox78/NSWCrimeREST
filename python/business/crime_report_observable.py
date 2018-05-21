from rx.subjects import Subject
from functools import wraps


OBSERVABLE_INSTANCE = Subject()


def observe_crime_report(fn):
    """
    Makes the result of the decorated function available via the singleton crime report subject.  

    For example, this enables new crime reports to be pushed out to registered websocket clients. 
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        crime_report = fn(*args, **kwargs)
        OBSERVABLE_INSTANCE.on_next(crime_report)
    return wrapper

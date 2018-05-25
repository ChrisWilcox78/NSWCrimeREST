from functools import wraps
from mongoengine import connect
from os import environ
from bson.errors import InvalidId
from mongoengine.queryset import DoesNotExist

DEFAULT_MONGO_HOST = "localhost"
DEFAULT_MONGO_PORT = "27017"


def db_connect(fn):
    """
    Connects to the mongo database server
    """
    @wraps(fn)
    def decorator(*args, **kwargs):
        connect("crime_reports", host=environ.get("MONGO_HOST", DEFAULT_MONGO_HOST),
                port=int(environ.get("MONGO_PORT", DEFAULT_MONGO_PORT)))
        return fn(*args, **kwargs)

    return decorator


def treat_not_found_as_none(fn):
    """
    Handles the exceptions thrown when a document cannot be found and returns None.
    """
    @wraps(fn)
    def decorator(*args, **kwargs):
        try:
            rval = fn(*args, **kwargs)
        except (InvalidId, DoesNotExist):
            return None
        return rval
    return decorator

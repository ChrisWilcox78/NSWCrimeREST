from functools import wraps
from mongoengine import connect
from os import environ

DEFAULT_MONGO_HOST = "localhost"
DEFAULT_MONGO_PORT = "27017"


def db_connect(fn):
    """
    Connects to the mongo database server
    """
    @wraps(fn)
    def wrapped(*args, **kwargs):
        connect("crime_reports", host=environ.get("MONGO_HOST", DEFAULT_MONGO_HOST),
                port=int(environ.get("MONGO_PORT", DEFAULT_MONGO_PORT)))
        return fn(*args, **kwargs)

    return wrapped

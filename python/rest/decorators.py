from functools import wraps
from threading import Thread
from .json_serializer import to_serializable
from json import dumps
from werkzeug.exceptions import NotFound


def json_content(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return dumps(fn(*args, **kwargs), default=to_serializable), {"Content-Type": "application/json"}

    return wrapper


def run_in_thread(fn):
    """
    Runs the wrapper function in a background thread, allowing the caller to move on.
    Useful for kicking off long-running processes.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs)
        thread.setDaemon = True
        thread.start()
    return wrapper


def treat_none_as_404(fn):
    """
    Raises werkzeug.exceptions.NotFound if the wrapped function returns None.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        rval = fn(*args, **kwargs)
        if rval is None:
            raise NotFound()
        return rval
    return wrapper

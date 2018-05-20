from functools import wraps
from threading import Thread
from rest.json_serializer import to_serializable
from json import dumps


def json_content(fn):
    @wraps(fn)
    def decorated(*args, **kwargs):
        return dumps(fn(*args, **kwargs), default=to_serializable), {"Content-Type": "application/json"}

    return decorated


def run_in_thread(fn):
    """
    Runs the decorated function in a background thread, allowing the caller to move on.
    Useful for kicking off long-running processes.
    """
    @wraps(fn)
    def decorated(*args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs)
        thread.setDaemon = True
        thread.start()
    return decorated

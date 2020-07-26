from flask import request
from functools import wraps

from chateaubriand.app.exception import BadRequest


def param_validate(schema: list):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for key in schema:
                value = request.args.get(key)
                if value is None:
                    break
            else:
                return fn(*args, **kwargs)
            raise BadRequest()

        return wrapper

    return decorator


GET_ASSIGNMENT = ["class"]

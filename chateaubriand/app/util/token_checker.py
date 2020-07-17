import jwt

from functools import wraps
from flask import request

from chateaubriand.app.exception import Unauthorized, AuthenticateFailed
from chateaubriand.config.app_config import ProductionLevelAppConfig


def available_token():
    def decorator(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):
            try: token = request.headers["Authorization"]
            except: raise AuthenticateFailed()

            type = jwt.decode(token, ProductionLevelAppConfig.SECRET_KEY)["admin"]
            if not type == "true": raise Unauthorized()

            return fn(*args, **kwargs)

        return wrapper

    return decorator

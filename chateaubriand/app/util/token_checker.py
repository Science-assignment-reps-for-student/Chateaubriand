import jwt

from functools import wraps
from flask import request

from chateaubriand.app.exception import Unauthorized, AuthenticateFailed
from chateaubriand.config.app_config import ProductionLevelAppConfig


def available_token(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            token = request.headers["Authorization"][7:]
        except:
            raise AuthenticateFailed()

        try:
            type = jwt.decode(token, ProductionLevelAppConfig.SECRET_KEY)["authority"]
        except:
            raise AuthenticateFailed()

        if not type == "ADMIN":
            raise Unauthorized()

        return fn(*args, **kwargs)

    return wrapper

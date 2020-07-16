import jwt

from functools import wraps
from flask import request

from chateaubriand.app.exception import Unauthorized, BadRequest
from chateaubriand.app.models.admin import AdminModel
from chateaubriand.config.app_config import ProductionLevelAppConfig


def available_token():
    def decorator(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):
            token = request.headers["Authorization"]
            if not token:
                raise BadRequest()

            admin_id = jwt.decode(token, ProductionLevelAppConfig.SECRET_KEY)

            if not AdminModel.query.filter_by().first():
                raise Unauthorized()

            return fn(*args, **kwargs)

        return wrapper

    return decorator

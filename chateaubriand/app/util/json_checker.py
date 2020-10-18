from flask import request
from functools import wraps

from chateaubriand.app.exception import BadRequest


def json_type_validate(json_schema: dict):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            json: dict = request.json
            if not json:
                raise BadRequest()

            for key, type_ in json_schema.items():
                value = json.get(key)
                if type(value) is not type_:
                    break
            else:
                return fn(*args, **kwargs)
            raise BadRequest()

        return wrapper

    return decorator


GET_ASSIGNMENT_JSON = {"assignment_id": str}
POST_ACCOUNT_JSON = {"email": str, "password": str, "name": str}
DELETE_ACCOUNT_JSON = {"email": str, "password": str}
POST_AUTH_JSON = {"email": str, "password": str}
POST_TOKEN_JSON = {"access_token": str, "refresh_token": str}

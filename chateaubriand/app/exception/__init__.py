from werkzeug.exceptions import HTTPException


class BaseException(HTTPException):
    pass


class Unauthorized(BaseException):
    code = 401
    description = "Wrong Auth"


class BadRequest(BaseException):
    code = 406
    description = "Bad Request"

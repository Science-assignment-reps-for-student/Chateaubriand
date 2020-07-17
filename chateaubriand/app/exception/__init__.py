from werkzeug.exceptions import HTTPException


class BaseException(HTTPException):
    pass


class BadRequest(BaseException):
    code = 400
    description = "Bad Request"


class AuthenticateFailed(BaseException):
    code = 401
    description = "AuthenticateFailed"


class Conflict(BaseException):
    code = 409
    description = "Conflict"


class BaseServerException(BaseException):
    code = 500


class ViewError(BaseServerException):
    # description = "View Error"
    pass

class ControllerError(BaseServerException):
    # description = "Controller Error"
    pass

class ServiceError(BaseServerException):
    # description = "Service Error"
    pass
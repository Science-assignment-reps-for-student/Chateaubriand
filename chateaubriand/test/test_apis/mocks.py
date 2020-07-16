import jwt


def jwt_mock(app, type):
    if type == "ADMIN":
        return jwt.encode({}, app.config["SECRET_KEY"], algorithm="HS256")
    elif type == "STUDENT":
        return jwt.encode({}, app.config["SECRET_KEY"], algorithm="HS256")

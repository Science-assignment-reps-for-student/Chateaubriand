import jwt

def jwt_mock(app):
    return jwt.encode({}, app.config["SECRET_KEY"], algorithm="HS256")
import jwt


def payload_builder(payload, user_type, token_type):
    payload["sub"] = "test@test.com"
    payload["type"] = token_type
    if user_type == "ADMIN": payload["admin"] = "true"
    return payload

def jwt_mock(app, user_type, token_type):
    payload = payload_builder({}, user_type, token_type)
    return jwt.encode(payload=payload, key=app.config["SECRET_KEY"], algorithm="HS256")
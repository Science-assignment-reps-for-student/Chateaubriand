import jwt


def payload_builder(payload, user_type, token_type, invalid):
    if invalid:
        payload["sub"] = 1
    else:
        payload["sub"] = 2
    payload["type"] = token_type
    payload["authority"] = user_type
    payload["sub"] = "test@test.test"
    return payload


def jwt_mock(app, user_type, token_type, invalid=False, bearer=False):
    payload = payload_builder({}, user_type, token_type, invalid)
    print(payload, app.config["SECRET_KEY"])
    token = jwt.encode(payload=payload, key=app.config["SECRET_KEY"], algorithm="HS256")
    if bearer: return str(f"Bearer {token.decode()}")
    return token.decode()

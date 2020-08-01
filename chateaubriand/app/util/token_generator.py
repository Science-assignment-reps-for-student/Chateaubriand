import jwt
import time

from chateaubriand.config.app_config import ProductionLevelAppConfig
from chateaubriand.app.exception import AuthenticateFailed


def generate_token(email, token_type, expire_time):
    payload = {
        "iat": int(time.time()),
        "exp": int(time.time()) + int(expire_time.seconds),
        "sub": email,
        "type": token_type,
        "authority": "ADMIN",
    }

    return jwt.encode(
        payload=payload, key=ProductionLevelAppConfig.SECRET_KEY, algorithm="HS256"
    )


def generate_access_token(email):
    token = generate_token(
        email, "access_token", ProductionLevelAppConfig.ACCESS_TOKEN_EXPIRE_TIME
    )
    return token.decode()


def generate_refresh_token(email):
    token = generate_token(
        email, "access_token", ProductionLevelAppConfig.REFRESH_TOKEN_EXPIRE_TIME
    )
    return token.decode()


def decode_token(token):
    return jwt.decode(token, ProductionLevelAppConfig.SECRET_KEY, verify=False)["sub"]

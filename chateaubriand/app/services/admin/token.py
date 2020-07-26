from chateaubriand.app.extensions import redis
from chateaubriand.app.exception import Unauthorized
from chateaubriand.app.util.token_generator import decode_token


class TokenService:
    @classmethod
    def check_token(cls, access_token, refresh_token):
        redis_db = redis.get_redis()
        email = decode_token(access_token)
        saved_refresh_token = redis_db.get(email)
        if not refresh_token == saved_refresh_token.decode():
            raise Unauthorized
        return email

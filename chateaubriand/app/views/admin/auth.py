from chateaubriand.app.extensions import redis
from chateaubriand.app.views import BaseView
from chateaubriand.app.util.token_generator import generate_access_token


class AuthView(BaseView):
    def __init__(self, email):
        self._email = email

    def get_access_token(self):
        return generate_access_token(self._email)

    def get_refresh_token(self):
        redis_db = redis.get_redis()
        return redis_db.get(self._email).decode()

    def data_merge(self):
        return (
            {
                "access_token": self.get_access_token(),
                "refresh_token": self.get_refresh_token(),
            },
            200
        )

    def get_view(self):
        return self.data_merge()

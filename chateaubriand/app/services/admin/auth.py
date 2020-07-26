import re

from werkzeug.security import check_password_hash

from chateaubriand.app.extensions import redis
from chateaubriand.app.models import AdminModel
from chateaubriand.app.exception import AuthenticateFailed, BadRequest
from chateaubriand.app.util.token_generator import generate_refresh_token


class AuthService:
    @classmethod
    def login(cls, email, password):
        cls.check_email_format(email)

        admin = AdminModel.query.filter_by(email=email).first()
        if not admin or not check_password_hash(admin.password, password):
            raise AuthenticateFailed()

        cls.register_refresh_token(email)

    @classmethod
    def register_refresh_token(cls, email):
        redis_db = redis.get_redis()
        redis_db.set(email, generate_refresh_token(email))

    @classmethod
    def check_email_format(cls, email):
        email_format = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        if not email_format.match(email):
            raise BadRequest

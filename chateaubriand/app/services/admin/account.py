import re

from werkzeug.security import generate_password_hash, check_password_hash

from chateaubriand.app.extensions import db, redis
from chateaubriand.app.models import AdminModel
from chateaubriand.app.exception import Conflict, BadRequest, NotFound


class AccountService:
    @classmethod
    def create_account(cls, email, password, name):
        cls.check_email_format(email)
        if AdminModel.query.filter_by(email=email).first():
            raise Conflict()

        account = AdminModel(
            email=email, password=generate_password_hash(password), name=name
        )
        db.session.add(account)
        db.session.commit()

    @classmethod
    def delete_account(cls, email, password):
        cls.check_email_format(email)
        account = AdminModel.query.filter_by(email=email).first()
        if not account or not check_password_hash(account.password, password):
            raise NotFound()

        redis_db = redis.get_redis()
        redis_db.delete(email)

        db.session.delete(account)
        db.session.commit()

    @classmethod
    def check_email_format(cls, email):
        email_format = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        if not email_format.match(email):
            raise BadRequest

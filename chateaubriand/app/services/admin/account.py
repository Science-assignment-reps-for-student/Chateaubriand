import re

from werkzeug.security import generate_password_hash

from chateaubriand.app.extensions import db
from chateaubriand.app.models.admin import AdminModel
from chateaubriand.app.exception import Conflict, BadRequest


class AccountService:
    @classmethod
    def create_account(cls, email, password, name):
        cls.check_email_format(email)
        if AdminModel.query.filter_by(email=email).first(): raise Conflict()

        admin = AdminModel(
            email=email,
            password=generate_password_hash(password),
            name=name
        )
        db.session.add(admin)
        db.session.commit()

    @classmethod
    def check_email_format(cls, email):
        email_format = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        if not email_format.match(email): raise BadRequest
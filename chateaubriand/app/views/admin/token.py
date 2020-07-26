from chateaubriand.app.views import BaseView
from chateaubriand.app.util.token_generator import generate_access_token


class TokenView(BaseView):
    def __init__(self, email):
        self._email = email

    def data_merge(self):
        return {"access_token": generate_access_token(self._email)}, 200

    def get_view(self):
        return self.data_merge()

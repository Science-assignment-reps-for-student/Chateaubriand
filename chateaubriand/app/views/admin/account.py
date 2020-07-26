from chateaubriand.app.views import BaseView
from chateaubriand.app.exception import ViewError


class AccountView(BaseView):
    def __init__(self, method):
        self._method = method

    def data_merge(self):
        if self._method == "POST":
            return {"description": "Created"}, 201
        elif self._method == "DELETE":
            return {"description": "Success"}, 200
        else:
            raise ViewError

    def get_view(self):
        return self.data_merge()

from test import BaseTestCase

from chateaubriand.app.views.admin.account import AccountView
from chateaubriand.app.exception import ViewError

class TestAccountView(BaseTestCase):
    def setUp(self):
        self.account_view_post = AccountView("POST")
        self.account_view_delete = AccountView("DELETE")
        self.account_view_error = AccountView("GET")

    def test_post(self):
        view = self.account_view_post.get_view()
        
        self.assertEqual(view, ({"description": "Created"}, 201))

    def test_delete(self):
        view = self.account_view_delete.get_view()

        self.assertEqual(view, ({"description": "Success"}, 200))

    def test_error(self):
        with self.assertRaises(ViewError):
            view = self.account_view_error.get_view()
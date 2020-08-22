from test import BaseTestCase

from unittest.mock import patch

from chateaubriand.app.views.admin.auth import AuthView
from chateaubriand.app.exception import ViewError

class TestAuthView(BaseTestCase):
    def setUp(self):
        self.auth_view_post = AuthView("test@test.test")

    @patch(
        'chateaubriand.app.views.admin.auth.AuthView.get_refresh_token',
        return_value = "ey.refresh.token")
    @patch(
        'chateaubriand.app.views.admin.auth.AuthView.get_access_token',
        return_value = "ey.access.token")
    def test_post(self, mock_generate_access_token, mock_get_refresh_token):
        view = self.auth_view_post.get_view()

        self.assertEqual(view, (
            {
                "access_token": "ey.access.token",
                "refresh_token": "ey.refresh.token"
            },
            200)
        )
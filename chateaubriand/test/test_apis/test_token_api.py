import os

from test import BaseTestCase
from test.test_apis.mocks import jwt_mock


class TokenTestCase(BaseTestCase):
    def __init__(self):
        self.path = "/admin/token"
        self.common_data_post = {
            "access_token": jwt_mock(self.app, "ADMIN", "access_token"),
            "refresh_token": jwt_mock(self.app, "ADMIN", "refresh_token")
        }

        self.invalid_data_post = {
            "access_token": 1
        }

        self.un_match_token_post = {
            "access_token": jwt_mock(self.app, "ADMIN", "access_token"),
            "refresh_token": jwt_mock(self.app, "ADMIN", "access_token", invalid=True)
        }

    def test_post(self):
        resp_200 = self.test_client.post(
            self.path,
            json = self.common_data_post
        )

        resp_400 = self.test_client.post(
            self.path,
            json = self.invalid_data_post
        )

        resp_403 = self.test_client.post(
            self.path,
            json = self.un_match_token_post
        )

        self.assertEqual(resp_200.status_code, 200)
        self.assertEqual(resp_400.status_code, 400)
        self.assertEqual(resp_403.status_code, 403)

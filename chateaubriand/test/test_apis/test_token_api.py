import os

from test import BaseTestCase
from test.test_apis.mocks import jwt_mock


class TokenTestCase(BaseTestCase):
    def test_post(self):
        path = "/admin/token"
        admin_token = jwt_mock(self.app, "ADMIN")

        resp_200 = self.test_client.post(path,
            json = {
                    "access_token": admin_token,
                    "refresh_token": admin_token
                })

        resp_400 = self.test_client.post(path,
            json = {"a": 123})

        resp_403 = self.test_client.post(path,
             json={
                 "access_token": admin_token,
                 "refresh_token": admin_token
             })

        self.assertEqual(resp_200.status_code, 200)
        self.assertEqual(resp_400.status_code, 400)
        self.assertEqual(resp_403.status_code, 403)
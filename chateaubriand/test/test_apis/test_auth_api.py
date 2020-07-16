import os

from test import BaseTestCase
from test.test_apis.mocks import jwt_mock


class AuthTestCase(BaseTestCase):
    def test_post(self):
        path = "/admin/auth"

        resp_200 = self.test_client.post(path,
        json = {
                "email": "admin@mallycrip.com",
                "password": "p@ssw0rd",
            })

        resp_400 = self.test_client.post(path,
        json = {"email": 123})

        self.assertEqual(resp_200.status_code, 200)
        self.assertEqual(resp_400.status_code, 400)
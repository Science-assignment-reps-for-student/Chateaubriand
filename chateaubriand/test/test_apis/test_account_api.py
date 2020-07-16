import os

from test import BaseTestCase
from test.test_apis.mocks import jwt_mock


class AccountTestCase(BaseTestCase):
    def test_post(self):
        path = "/admin/account"

        resp_201 = self.test_client.post(path,
        json = {
                "email": "admin@mallycrip.com",
                "password": "p@ssw0rd",
                "name": "정우영"
            })

        resp_400 = self.test_client.post(path,
        json = {"email": 123})

        self.assertEqual(resp_201.status_code, 201)
        self.assertEqual(resp_400.status_code, 400)

    def test_delete(self):
        path = "/admin/account"

        admin_token = jwt_mock(self.app, "ADMIN")

        resp_200 = self.test_client.delete(path,
            json={
                "email": "admin@mallycrip.com",
                "password": "p@ssw0rd"
            },
            header={"Authorization": "Bearer"+ admin_token})

        resp_401 = self.test_client.delete(path,
           json={
               "email": "admin@mallycrip.com",
               "password": "p@ssw0rd"
           })

        self.assertEqual(resp_200.status_code, 200)
        self.assertEqual(resp_401.status_code, 401)
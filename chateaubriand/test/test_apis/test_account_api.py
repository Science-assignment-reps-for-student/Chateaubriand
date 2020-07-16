import os

from test import BaseTestCase
from test.test_apis.mocks import jwt_mock


class AccountTestCase(BaseTestCase):
    def __init__(self):
        self.path = "/admin/account"
        self.duplicate_body_post = {
            "email": "same@same.same",
            "password": "password",
            "name": "김중복"
        }

        self.common_body_post = {
            "email": "test@test.com",
            "password": "test",
            "name": "테스트",
        }

        self.common_body_delete = {
            "email": "test@test.com",
            "password": "test"
        }

        self.invalid_body_post = {
            "email": 1,
            "password": 1
        }

        self.invalid_body_delete = {
            "email": 1,
            "password": 1
        }

        self.common_header = {
            "Authorization": "Bearer" + jwt_mock(self.app, "ADMIN")
        }



    def setUp(self):
        self.test_client.post(
            self.path,
            json = self.duplicate_body_post
        )

    def test_post(self):
        resp_201 = self.test_client.post(
            self.path,
            json = self.common_body_post
        )

        resp_400 = self.test_client.post(
            self.path,
            json = self.invalid_body_post
        )

        resp_409 = self.test_client.post(
            self.path,
            json = self.duplicate_body_post
        )

        self.assertEqual(resp_201.status_code, 201)
        self.assertEqual(resp_400.status_code, 400)
        self.assertEqual(resp_409.status_code, 409)

    def test_delete(self):
        resp_200 = self.test_client.delete(
            self.path,
            json = self.common_body_delete,
            header = self.common_header,
        )

        resp_400 = self.test_client.delete(
            self.path,
            json = self.invalid_body_delete,
            header = self.common_header
        )

        resp_401 = self.test_client.delete(
            self.path,
            json = self.common_body_delete
        )

        self.assertEqual(resp_200.status_code, 200)
        self.assertEqual(resp_400.status_code, 400)
        self.assertEqual(resp_401.status_code, 401)

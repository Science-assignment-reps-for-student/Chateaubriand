from test import BaseTestCase
from test.test_apis.mocks import jwt_mock


class AuthTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.path = "/admin/auth"
        self.common_body_post = {"email": "test@test.test", "password": "password"}

        self.invalid_body_post = {"email": 123}

        self.invalid_info_body_post = {
            "email": "test@test.test",
            "password": "wrong_password",
        }

        self.test_client.post(
            "admin/account",
            json={"email": "test@test.test", "password": "password", "name": "테스트"}
        )

    def tearDown(self):
        self.test_client.delete(
            "admin/account",
            json={"email": "test@test.test", "password": "password"},
            headers={"Authorization": jwt_mock(self.app, "ADMIN", "access_token", bearer=True)}
        )

    def test_post(self):
        resp_200 = self.test_client.post(self.path, json=self.common_body_post)

        resp_400 = self.test_client.post(self.path, json=self.invalid_body_post)

        resp_401 = self.test_client.post(self.path, json=self.invalid_info_body_post)

        self.assertEqual(resp_200.status_code, 200)
        self.assertEqual(resp_400.status_code, 400)
        self.assertEqual(resp_401.status_code, 401)

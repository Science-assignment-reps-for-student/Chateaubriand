from test import BaseTestCase
from test.test_apis.mocks import jwt_mock


class PersonalAssignmentTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.path = "/admin/personal-assignment"
        self.common_get = {
            "class": 1
        }

        self.invalid_get = {
            "class": "1"
        }

        self.common_header = {
            "Authorization": jwt_mock(self.app, "ADMIN", "access_token")
        }

        self.invalid_header = {
            "Authorization": jwt_mock(self.app, "STUDENT", "access_token")
        }

    def test_get(self):
        resp_200 = self.test_client.get(
            self.path,
            json=self.common_get,
            headers=self.common_header
        )

        resp_400 = self.test_client.get(
            self.path,
            json=self.invalid_get,
            headers=self.common_header
        )

        resp_401 = self.test_client.get(
            self.path,
            json=self.common_get
        )

        resp_403 = self.test_client.get(
            self.path,
            json=self.common_get,
            headers=self.invalid_header,
        )

        self.assertEqual(resp_200.status_code, 200)
        self.assertEqual(resp_400.status_code, 400)
        self.assertEqual(resp_401.status_code, 401)
        self.assertEqual(resp_403.status_code, 403)

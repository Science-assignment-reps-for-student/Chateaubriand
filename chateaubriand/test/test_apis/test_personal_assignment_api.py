import os

from test import BaseTestCase
from test.test_apis.mocks import jwt_mock


class PersonalAssignmentTestCase(BaseTestCase):
    def test_get(self):
        admin_token = jwt_mock(self.app, "ADMIN")
        path = "/admin/personal-assignment"

        resp_200 = self.test_client.get(
            path, json={"class": 1}, headers={"authorization": "Bearer" + admin_token}
        )

        resp_400 = self.test_client.get(
            path, json={"class": "1"}, headers={"authorization": "Bearer" + admin_token}
        )

        resp_401 = self.test_client.get(path, json={"class": 1})

        resp_403 = self.test_client.get(
            path,
            json={"class": 1},
            headers={"authorization": "Bearer" + jwt_mock(self.app, "STUDENT")},
        )

        self.assertEqual(resp_200.status_code, 200)
        self.assertEqual(resp_400.status_code, 400)
        self.assertEqual(resp_401.status_code, 401)
        self.assertEqual(resp_403.status_code, 403)

from test import BaseTestCase
from test.test_apis.mocks import jwt_mock


class ExperimentAssignmentTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.path = "/admin/experiment-assignment?class=1"

        self.common_header = {
            "Authorization": jwt_mock(self.app, "ADMIN", "access_token", bearer=True)
        }

        self.invalid_header = {
            "Authorization": jwt_mock(self.app, "STUDENT", "access_token", bearer=True)
        }

    def test_get(self):
        resp_200 = self.test_client.get(
            self.path, json=self.common_get, headers=self.common_header
        )

        resp_403 = self.test_client.get(
            self.path, json=self.common_get, headers=self.invalid_header,
        )

        self.assertEqual(resp_200.status_code, 200)
        self.assertEqual(resp_403.status_code, 403)

import os

from test import BaseTestCase
from test.test_apis.mocks import jwt_mock


class ExperimentAssignmentTestCase(BaseTestCase):
    def test_get(self):
        token = jwt_mock(self.app)
        path = "/experiment-assignment"

        resp_200 = self.test_client.get(path, 
        json = {"class": 1}, 
        headers={"authorization": token})

        resp_401 = self.test_client.get(path, 
        json = {"class": 1})

        resp_406 = self.test_client.get(path, 
        json = {"class": "1"}, 
        headers={"authorization": token})

        self.assertEqual(resp_200.status_code, 200)
        self.assertEqual(resp_401.status_code, 401)
        self.assertEqual(resp_406.status_code, 406)



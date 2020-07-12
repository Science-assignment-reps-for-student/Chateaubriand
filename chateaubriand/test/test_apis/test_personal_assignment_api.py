import os

from test import BaseTestCase
from test.test_apis.mocks import jwt_mock


class PersonalAssignmentTestCase(BaseTestCase):
    def test_get(self):
        token = jwt_mock(self.app)

        resp = self.test_client.get('/personal-assignment', 
        json = {"class": 1}, 
        headers={"authorization": token})

        self.assertEqual(resp.status_code, 200)
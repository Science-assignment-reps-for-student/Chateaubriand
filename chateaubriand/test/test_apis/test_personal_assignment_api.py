import os
import jwt

from test import BaseTestCase


class PersonalAssignmentTestCase(BaseTestCase):
    def test_get(self):
        token = jwt.encode({},self.app.config["SECRET_KEY"] ,algorithm="HS256" )

        resp = self.test_client.get('/personal-assignment', 
        json = {"class": 1}, 
        headers={"authorization": token})

        self.assertEqual(resp.status_code, 200)
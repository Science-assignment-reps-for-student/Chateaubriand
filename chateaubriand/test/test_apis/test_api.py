import os

from chateaubriand.test import BaseTestCase


class Api1TestCase(BaseTestCase):
    # def test_created(self):
    #     resp = self.test_client.post('/create', json={
    #         "id": "mally",
    #         "password": "test"
    #     })

    #     self.assertEqual(resp.status_code, 201)
    def test_example(self):
        self.assertEqual(1, 1)
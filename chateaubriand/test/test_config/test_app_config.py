import os

from test import BaseTestCase


class AppConfigTestCase(BaseTestCase):
    def test_config(self):
        self.assertEqual(self.app.config["DEBUG"], False)
        self.assertEqual(self.app.config["ENV"], "production")
        self.assertEqual(self.app.config["SECRET_KEY"], os.getenv("SECRET_KEY"))

    def test_db_config_exist(self):
        self.assertNotEqual(os.getenv("DATABASE_USERNAME"), None)
        self.assertNotEqual(os.getenv("DATABASE_PASSWORD"), None)

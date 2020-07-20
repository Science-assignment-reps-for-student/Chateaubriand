import unittest

from chateaubriand.app import create_app
from chateaubriand.config.redis_config import TestRedisConfig
from chateaubriand.config.app_config import TestLevelAppConfig
from chateaubriand.config.db_config import TestDBConfig


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestLevelAppConfig, TestDBConfig, TestRedisConfig)
        self.test_client = self.app.test_client()

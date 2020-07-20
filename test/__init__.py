import unittest

from chateaubriand.app import create_app
from chateaubriand.config.redis_config import LocalRedisConfig
from chateaubriand.config.app_config import DevLevelAppConfig, ProductionLevelAppConfig
from chateaubriand.config.db_config import LocalDBConfig


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(LocalRedisConfig, ProductionLevelAppConfig, LocalDBConfig)
        self.test_client = self.app.test_client()

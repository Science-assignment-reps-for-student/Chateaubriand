from waitress import serve

from chateaubriand.app import create_app
from chateaubriand.config.app_config import DevLevelAppConfig
from chateaubriand.config.db_config import LocalDBConfig
from chateaubriand.config.redis_config import LocalRedisConfig


if __name__ == "__main__":
    app = create_app(DevLevelAppConfig, LocalDBConfig, LocalRedisConfig)
    app.run()

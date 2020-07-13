from waitress import serve

from chateaubriand.app import create_app
from chateaubriand.const.run_setting import RUN_SETTINGS
from chateaubriand.config.app_config import ProductionLevelAppConfig
from chateaubriand.config.db_config import RemoteDBConfig


if __name__ == "__main__":
    app = create_app(ProductionLevelAppConfig, RemoteDBConfig)
    serve(app, **RUN_SETTINGS)
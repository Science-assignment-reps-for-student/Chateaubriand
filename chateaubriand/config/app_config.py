import os
import datetime


class DefaultAppConfig:
    ENV = "development"
    DEBUG = True
    SECRET_KEY = ""
    ACCESS_TOKEN_EXPIRE_TIME = datetime.timedelta(minutes=10)
    REFRESH_TOKEN_EXPIRE_TIME = datetime.timedelta(days=14)


class DevLevelAppConfig(DefaultAppConfig):
    SECRET_KEY = "temporarysecretkey"


class ProductionLevelAppConfig(DefaultAppConfig):
    ENV = "production"
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY")


class TestLevelAppConfig(ProductionLevelAppConfig):
    pass

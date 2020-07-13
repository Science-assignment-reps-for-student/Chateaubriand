import os


class DefaultAppConfig:
    ENV = "development"
    DEBUG = True
    SECRET_KEY = ""


class DevLevelAppConfig(DefaultAppConfig):
    SECRET_KEY = "temporarysecretkey"


class ProductionLevelAppConfig(DefaultAppConfig):
    ENV = "production"
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY")
import os


def build_database_uri(username, password, host):
    return "mysql://" + username + ":" + password + "@" + host


class LocalDBConfig:
    LOCAL_DATABASE_USERNAME = "root"
    LOCAL_DATABASE_PASSWORD = os.getenv("LOCAL_DATABASE_PASSWORD")
    LOCAL_DATABASE_HOST = os.getenv("LOCAL_DATABASE_HOST")
    SQLALCHEMY_DATABASE_URI = build_database_uri(LOCAL_DATABASE_USERNAME, LOCAL_DATABASE_PASSWORD, LOCAL_DATABASE_HOST)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class RemoteDBConfig:
    DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE_HOST = os.getenv("DATABASE_HOST")
    SQLALCHEMY_DATABASE_URI = build_database_uri(DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
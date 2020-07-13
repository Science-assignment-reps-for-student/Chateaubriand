import os


class LocalDBConfig:
    DATABASE_USERNAME = os.getenv("LOCAL_DATABASE_USERNAME")
    DATABASE_PASSWORD = os.getenv("LOCAL_DATABASE_PASSWORD")
    DATABASE_HOST = os.getenv("LOCAL_DATABASE_HOST")
    SQLALCHEMY_DATABASE_URI = (
        "mysql://root:"
        + DB_PASSWORD
        + "@scarfs.cm63idi6gyr1.ap-northeast-2.rds.amazonaws.com/scarfs_production"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class RemoteDBConfig:
    DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE_HOST = os.getenv("DATABASE_HOST")
    SQLALCHEMY_DATABASE_URI = (
        "mysql://root:"
        + DB_PASSWORD
        + "@scarfs.cm63idi6gyr1.ap-northeast-2.rds.amazonaws.com/scarfs_production"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
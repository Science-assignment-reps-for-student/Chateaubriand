import os


class LocalRedisConfig:
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_PASSWORD = ""
    REDIS_DB = 0


class RemoteRedisConfig:
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = os.getenv("REDIS_PORT")
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
    REDIS_DB = os.getenv("REDIS_DB")


class TestRedisConfig:
    REDIS_HOST = os.getenv("TEST_REDIS_HOST")
    REDIS_PORT = os.getenv("TEST_REDIS_PORT")
    REDIS_PASSWORD = os.getenv("TEST_REDIS_PASSWORD")
    REDIS_DB = os.getenv("TEST_REDIS_DB")

from redis import StrictRedis


class RedisAdapter:
    def __init__(self):
        self.redis = None

    def init_app(self, app):
        self.redis = StrictRedis(
            host=app.config["REDIS_HOST"],
            port=app.config["REDIS_PORT"],
            password=app.config["REDIS_PASSWORD"],
            db=app.config["REDIS_DB"],
        )

    def get_redis(self):
        return self.redis

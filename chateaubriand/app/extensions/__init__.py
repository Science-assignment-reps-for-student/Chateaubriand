import logging

from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from chateaubriand.app.extensions.redis_adapter import RedisAdapter


db = SQLAlchemy()
cors = CORS()
redis = RedisAdapter()


logger = logging.getLogger("waitress")
logger.setLevel(logging.INFO)
logging.basicConfig(
    filename="logs/access.log", format="%(asctime)s %(levelname)s %(message)s"
)

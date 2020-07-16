import logging
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
jwt = JWTManager()
cors = CORS()
logger = logging.getLogger("waitress")
logger.setLevel(logging.INFO)
logging.basicConfig(
    filename="logs/access.log", format="%(asctime)s %(levelname)s %(message)s"
)

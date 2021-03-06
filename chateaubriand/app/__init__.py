from flask import Flask

from chateaubriand.app import extensions
from chateaubriand.app.controllers.admin import admin_blueprint
from chateaubriand.app.hooks.after_request import after_request


def register_hooks(app: Flask):
    app.after_request(after_request)


def register_controllers(app: Flask):
    app.register_blueprint(admin_blueprint)


def register_extensions(app: Flask):
    extensions.cors.init_app(app)
    extensions.db.init_app(app)
    extensions.redis.init_app(app)


def create_app(*config_cls) -> Flask:
    app = Flask(__name__)

    for config in config_cls:
        app.config.from_object(config)

    register_extensions(app)
    register_hooks(app)
    register_controllers(app)

    return app

from flask import Flask

from chateaubriand.app import extensions
from chateaubriand.app.hooks.after_request import after_request


def register_hooks(app: Flask)
    app.after_request(after_request)


def register_controllers(app: Flask):
    pass


def register_extensions(app: Flask):
    extensions.cors.init_app(app)
    extensions.db.init_app(app)
    extensions.jwt.init_app(app)


def create_app(*config_cls) -> Flask:
    app = Flask()

    for config in config_cls:
        flask_app.config.from_object(config)
    
    register_hooks(app)
    register_controllers(app)
    register_extensions(app)

    return app
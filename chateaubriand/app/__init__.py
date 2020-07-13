from flask import Flask


def register_hooks(app: Flask)
    pass


def register_controllers(app: Flask):
    pass


def register_extensions(app: Flask):
    pass


def create_app(*config_cls) -> Flask:
    app = Flask()

    for config in config_cls:
        flask_app.config.from_object(config)
    
    register_hooks(app)
    register_controllers(app)
    register_extensions(app)

    return app
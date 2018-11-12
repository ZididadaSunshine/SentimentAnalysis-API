from flask import Flask

from .config import configurations


def create_app(config_name):
    # Check if configuration is valid
    if config_name not in configurations:
        raise ValueError(f'{config_name} is not a valid configuration.')

    app = Flask(__name__)
    app.config.from_object(configurations[config_name])

    return app

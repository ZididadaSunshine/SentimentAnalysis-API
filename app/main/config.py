import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_key')
    DEBUG = False


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True


class TestingConfig(Config):
    ENV = 'development'
    TESTING = True


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False


configurations = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)


tokenizer_path = os.environ.get('TOKENIZER_PATH')
serving_url = os.environ.get('SERVING_URL')

secret = Config.SECRET_KEY

import os

class Config:

    SECRET_KEY = 'carexfm'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://carey:carexfm.@localhost/pitches'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class TestConfig(Config):
    pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://carey:carexfm.@localhost/pitches'
    DEBUG = True



config_options = {
    'development': DevConfig,
    'production' : ProdConfig,
    'test' : TestConfig
}

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'seu-secret-key'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'FLASK_CONFIG': DevelopmentConfig,
    'default': DevelopmentConfig
}

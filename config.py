import os
basedir = os.path.abspath(os.path.dirname(__file__))

class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        "sqlite:///tips.db"
    SQLALCHEMY_ECHO = True

class TestingConfig():
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        "sqlite:///testing.db"
    SQLALCHEMY_ECHO = True

class ProductionConfig():
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        "sqlite:///tipsproduction.db"

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
import os

class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    # TODO: create secret key func and create secret key at creation if the file
    SECRET = "ICH BIN EIN SECRET KEY"
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"

class DevelopmentConfig(Config):
    """Config for dev"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"

class TestingConfig(Config):
    """Config for testing"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///testing.db"

class StagineConfig(Config):
    """Config for staging"""
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagineConfig,
    'production': ProductionConfig
}

import os
from enum import Enum
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class EnvStrings(Enum):
    APP_SETTINGS = "APP_SETTINGS"
    ALLOWED_EXTENSIONS = "ALLOWED_EXTENSIONS"
    UPLOAD_FOLDER = "UPLOAD_FOLDER"

from distutils.debug import DEBUG
from msilib.schema import Class
import os
from os import environ
from unittest.mock import DEFAULT

class Config(object):
    DEBUG = False
    TESTING = False

    basedir =  os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'L$ab7seOp8*d]c'

    DB_NAME = ""
    DB_USERNAME = ""
    DB_PASSWORD = ""

    UPLOADS = "app/static/uploads"
    
    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = ""
    DB_USERNAME = ""
    DB_PASSWORD = ""

    UPLOADS = "app/static/uploads"
    SESSION_COOKIE_SECURE = False

class DebugConfig(Config):
    DEBUG = False
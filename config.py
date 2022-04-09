import os

class Config(object):
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY',
                    default=b'\x80\t\xb3Y\x94Q\xb1\xab\\Q\x89\xd3\xd4\xddAV\xbf\x02\xe30\x0c\xa2)\x01\xac\x0b\x1b\xc6\xc0H\xb0*')

class ProductionConfig(Config):
    FLASK_ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
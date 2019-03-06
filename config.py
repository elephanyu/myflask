import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'hard to guess string'
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '742453618@qq.com'
    MAIL_PASSWORD = ''
    MYFLASK_MAIL_SUBJECT_PREFIX = '[MYFLASK]'
    MYFLASK_MAIL_SENDER = 'MYFLASK_ADMIN <742453618@qq.com>>'
    MYFLASK_ADMIN = '742453618@qq.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MYFLASK_POSTS_PER_PAGE = 5
    MYFLASK_FOLLOWERS_PER_PAGE = 5
    MYFLASK_COMMENTS_PER_PAGE = 3
    MYFLASK_SLOW_DB_QUERY_TIME = 0.5


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

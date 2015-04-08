#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'c48b1b874cd28fc5f88773b9f847ca8311ef5bfb8fb3efbe'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/urls"
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'urls.db')


class TestingConfig(Config):
    TESTING = True


LANGUAGES = {
    'en': 'English',
    'de': 'Deutsch',
    'ar': 'عربي',
}

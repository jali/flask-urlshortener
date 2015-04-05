# -*- coding: utf-8 -*-
# imports

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.babel import Babel, gettext
import os

# config

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
babel = Babel(app)

from . import views


#!/usr/bin/python
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.babel import Babel
import os

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
babel = Babel(app)

from . import views


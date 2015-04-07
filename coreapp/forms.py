#!/usr/local/bin/python

from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, url, Optional


class ShortForm(Form):
	long_url = TextField('long_url', validators=[DataRequired(), url(), Optional(strip_whitespace=True)])


from flask_wtf import Form
from wtforms import TextField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url, Optional

class ShortForm(Form):
	long_url = TextField('long_url', validators=[DataRequired(), url(), Optional(strip_whitespace=True)])

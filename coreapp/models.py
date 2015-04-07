#!/usr/bin/python

from coreapp import db
from datetime import datetime


class Short(db.Model):
	__tablename__ = "short"

	id = db.Column(db.Integer, db.Sequence('short_seq', start=1, increment=1), primary_key=True)
	short_url = db.Column(db.String(30), nullable=False)
	long_url = db.Column(db.Text, nullable=False)
	created = db.Column(db.DateTime, default=datetime.utcnow)
	views = db.Column(db.Integer, default=0)


	def __init__(self, short_url, long_url):
		self.short_url = short_url
		self.long_url = long_url


	def __repr__(self):
		return "<Short('%s', '%s')>" % (self.long_url, self.views)

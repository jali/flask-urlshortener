#!/usr/bin/python

from flask.ext.testing import TestCase
from coreapp import app, db
from coreapp.models import Short

class BaseTestCase(TestCase):
	""" Base test case"""
	
	def create_app(self):
		app.config.from_object('config.TestingConfig')
		return app

	def setUp(self):
		db.create_all()
		db.session.add(Short("1", "http://twitter.com/jalalmaqdisi"))
		db.session.add(Short("2", "http://jal.al"))
		db.session.commit()

	def tearDown(self):
		db.session.remove()
		db.drop_all()



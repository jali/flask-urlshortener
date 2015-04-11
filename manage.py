#!/usr/bin/python

import unittest
import os

from flask.ext.script import Manager
from coreapp import app, db

app.config.from_object(os.environ['APP_SETTINGS'])

manager = Manager(app)

@manager.command
def test():
	""" Runs the unit tests without coverage."""
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity=2).run(tests)



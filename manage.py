#!/usr/bin/python

import unittest
import os

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from coreapp import app, db

app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
	""" Runs the unit tests without coverage."""
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
	manager.run()

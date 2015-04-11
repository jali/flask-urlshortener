#!/usr/bin/python
# -*- coding: utf-8 -*-
from coreapp import db
from coreapp.models import Short

db.drop_all()
db.create_all()
db.session.add(Short("1", "http://twitter.com/jalalmaqdisi"))
db.session.add(Short("2", "https://github.com/maqdisi/Flask-URLShortener"))
db.session.commit()


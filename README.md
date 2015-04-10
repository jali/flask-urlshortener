# URL Shortener
Travis CI Status [![Build Status](https://travis-ci.org/maqdisi/Flask-URLShortener.svg?branch=master)](https://travis-ci.org/maqdisi/Flask-URLShortener.svg)

This URL Shortener is a service that takes long URL and squeezes it into short characters to make a link that is easier to share, tweet, or email to friends.

The app is using python flask, bootstrap and postgresql database. The core function is here: [https://github.com/maqdisi/python-url-shortener](https://github.com/maqdisi/python-url-shortener)

This service supports internationalization (i18n) such as English, Deutsch and Arabic عربي

![Default language: English](https://raw.githubusercontent.com/maqdisi/Flask-URLShortener/master/screenshots/screenshot-en.png)


Installation:
-------------
Create your postgres database.
As per config.py setting the database name is: urls

	psql
	CREATE DATABASE urls;

Follow the steps below:

	$ git clone https://github.com/maqdisi/Flask-URLShortener
	$ cd Flask-URLShortener
	$ workon <your virtual environment>
	$ export APP_SETTINGS="config.DevelopmentConfig"

Add your psql to your machine's path

*Example for psql on Mac OS X*

	export PATH=/Applications/Postgres.app/Contents/Versions/9.4/bin:$PATH
	
Continue by executing the folowing commands:

	$ pip install psycopg2
	$ pip install -r requirements.txt
	$ python db_create.db


To run the app:
---------------
	$ python web.py

Goto: [http://localhost:8081](http://localhost:8081)



**German locale:**

![Detecting language: German](https://raw.githubusercontent.com/maqdisi/Flask-URLShortener/master/screenshots/screenshot-de.png)

**Arabic locale:**

![Detecting language: Arabic](https://raw.githubusercontent.com/maqdisi/Flask-URLShortener/master/screenshots/screenshot-ar.png)



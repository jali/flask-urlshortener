# URL Shortener
----------------
Travis CI Status [![Build Status](https://travis-ci.org/jali/flask-urlshortener.svg?branch=master)](https://travis-ci.org/jali/flask-urlshortener)

This is a service that takes long URL and squeezes it into short characters to make a link that is easier to share, tweet, or email to friends.

The app is using python flask, bootstrap and postgresql database.

This service supports internationalization (i18n) such as English, German (Deutsch) and Arabic (عربي)


Installation:
-------------
Create your postgres database.
As per config.py setting the database name is: urls

	$ su - postgres
	$ psql
	$ CREATE DATABASE urls;

Follow the steps below:

	$ git clone https://github.com/jali/flask-urlshortener
	$ cd flask-urlshortener
	$ workon <your virtual environment>
	$ export APP_SETTINGS="config.DevelopmentConfig"

Add your psql to your machine's path

*Example for psql on Mac OS X*

	export PATH=/Applications/Postgres.app/Contents/Versions/9.4/bin:$PATH
	
Continue by executing the folowing commands:

	$ pip install -r requirements.txt
	$ python db_create.py

Run the tests:
--------------
	$ python manage.py test
	

To run the app:
---------------
	$ python web.py

Goto: [http://localhost:8081](http://localhost:8081)

OR you can use runserver like this:

	$ python manage.py runserver
Then goto: [http://localhost:5000](http://localhost:5000)


Update translation:
-------------------
If you change text or values, you need to run the following inside your vitrual env.
	
	$ pybabel update -i messages.pot -d coreapp/translations
	$ pybabel compile -d coreapp/translations

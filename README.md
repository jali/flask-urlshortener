# Flask-URLShortener
Flask URL shortener using wtforms, sqlalchemy, babel, bootstrap and postgresql

![Default language: English](https://raw.githubusercontent.com/maqdisi/Flask-URLShortener/master/screenshots/screenshot-en.png)


Installation:
-------------
Create your postgres database.
As per config.py setting the database is: urls

	psql
	CREATE DATABASE urls;

Follow the steps below:

	* git clone https://github.com/maqdisi/Flask-URLShortener
	* cd Flask-URLShortener
	* workon <your virtual environment>
	* export APP_SETTINGS="config.DevelopmentConfig"

Add your psql to your machine's path

*Example for psql on Mac OS X*

	export PATH=/Applications/Postgres.app/Contents/Versions/9.4/bin:$PATH
	
Continue by executing the folowing commands:

	* pip install psycopg2
	* pip install -r requirements.txt
	* run python db-create.db


To run the app:
---------------
	run python web.py

Goto: [http://localhost:8081](http://localhost:8081)


German:
-------
![Detecting language: German](https://raw.githubusercontent.com/maqdisi/Flask-URLShortener/master/screenshots/screenshot-de.png)

Arabic:
-------
![Detecting language: Arabic](https://raw.githubusercontent.com/maqdisi/Flask-URLShortener/master/screenshots/screenshot-ar.png)

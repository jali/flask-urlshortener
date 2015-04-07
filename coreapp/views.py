#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, request, session, url_for, abort
from sqlalchemy import Sequence
from coreapp import app, db, babel
from config import LANGUAGES
from forms import ShortForm
from models import Short


def base60encode(n):
        s = ""
        m = "0123456789_abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"
        if (n == 0):
                return 0
        while (n > 0):
                d = n % 60
                s = m[d] + s
                n = (n-d)/60
        return s


@app.route("/", methods=['GET', 'POST'])
def home():
        short = None
        links = None
        form = ShortForm()
        if form.validate_on_submit():
                nextId = db.session.execute("select last_value from short_seq").fetchone()[0] + 1
                short = base60encode(nextId)
                sh = Short(
                    short_url=short,
                    long_url=form.long_url.data
                )
                db.session.add(sh)
                db.session.commit()

        links = Short.query.order_by('created desc').all()
        return render_template('home.html', links=links, short=short, lang=get_locale(), form=form)


@app.route("/about")
def about():
        return render_template('about.html')


@app.route("/<token>")
def expand(token):
	record = Short.query.filter_by(short_url=token).first_or_404()
	record.views += 1
	db.session.commit()
	return redirect(record.long_url, 301)


@app.errorhandler(404)
def page_not_found(e):
        return render_template('404.html', lang=get_locale()), 404


@babel.localeselector
def get_locale():
        return request.accept_languages.best_match(LANGUAGES.keys())


#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from flask import render_template

from sayhello import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500

#!/usr/bin/env python
# coding=utf-8

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Требуется только если приложение использует подписанные сессии.
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
CSRF_ENABLED = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

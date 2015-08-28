__author__ = 'dimitris'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache


app = Flask(__name__)
app.config.from_pyfile('../Application/app_configuration.py')
db = SQLAlchemy(app)
cache = Cache(app)
from Application import models, views
__author__ = 'dimitris'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('../Application/app_configuration.py')
db = SQLAlchemy(app)

from Application import models, views
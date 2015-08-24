__author__ = 'dimitris'

import os

basedir = os.path.abspath(os.path.dirname(__file__))
TESTING = True
DB_NAME = 'testing_database.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, DB_NAME)
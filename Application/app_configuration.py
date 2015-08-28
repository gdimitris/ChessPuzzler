__author__ = 'dimitris'

import os

# Flask Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = 'knaskndfknasdfiaosifoaignaosdnfoasodfnaodgnas'
PREFERRED_URL_SCHEME = 'https'

#SqlAlchemy Configuration
DB_NAME = 'puzzles.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, DB_NAME)

#Cache Configuration
CACHE_TYPE = 'simple'
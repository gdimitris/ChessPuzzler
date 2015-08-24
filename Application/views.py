__author__ = 'dimitris'

from Application import app

@app.route('/', methods=['GET'])
def hello():
    return "hello world"
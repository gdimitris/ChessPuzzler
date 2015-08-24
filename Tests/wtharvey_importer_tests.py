__author__ = 'dimitris'

import unittest
import Application.views as application
from Application import app, db


class HarveyImporterTests(unittest.TestCase):

    def setUp(self):
        app.config.from_pyfile('../Tests/test_configuration.py')
        self.app = application.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def testItWorks(self):
        self.assertTrue(True)
__author__ = 'dimitris'

import unittest
import time
from Tests.wtharvey_importer_tests import HarveyImporterTests
from coverage import coverage


coverage_obj = coverage(branch=True, omit=['Virtual_Environment/*', 'Tests/*'])
coverage_obj.start()

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(HarveyImporterTests))

runner = unittest.TextTestRunner()
runner.run(test_suite)

coverage_obj.stop()
coverage_obj.save()

time.sleep(0.1)
print '\n Coverage Report: \n'
coverage_obj.report()
print '\n Report in HTML: http://localhost:63342/ChessPuzzlerBackend/tmp/coverage/index.html'
coverage_obj.html_report(directory='../tmp/coverage')
coverage_obj.erase()
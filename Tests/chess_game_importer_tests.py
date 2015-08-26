__author__ = 'dimitris'

import unittest
import Application.views as application
from Application.models import ChessPuzzle
from Application.chess_game_importer import ChessGameImporter
from Application import app, db


class HarveyImporterTests(unittest.TestCase):

    def setUp(self):
        app.config.from_pyfile('../Tests/test_configuration.py')
        self.app = application.app.test_client()
        self.importer = ChessGameImporter()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def testReadOneEntry(self):
        desc = 'Wilfried Paulsen vs Adolf Anderssen, Frankfurt, 1878'
        fen = '5rk1/1p1q2bp/p2pN1p1/2pP2Bn/2P3P1/1P6/P4QKP/5R2 w - - 1 0'
        solution = '1. Qxf8+ Bxf8 2. Rxf8#'
        expected_object = ChessPuzzle(description=desc, fen=fen, solution=solution)
        result_list = self.importer.parse_file_for_chess_entries('Test_Resources/one_entry.txt')
        self.assertEqual(expected_object, result_list[0])

    def testReadSevenEntries_ReturnsCorrectFifthEntry(self):
        fifth_desc = 'Gustav Neumann vs Carl Mayet, Berlin, 1866'
        fifth_fen = '5rkr/pp2Rp2/1b1p1Pb1/3P2Q1/2n3P1/2p5/P4P2/4R1K1 w - - 1 0'
        fifth_solution = '1. Qxg6+ fxg6 2. Rg7#'
        expected_object = ChessPuzzle(description=fifth_desc, fen=fifth_fen, solution=fifth_solution)
        result_list = self.importer.parse_file_for_chess_entries('Test_Resources/m8n2.txt')
        self.assertEqual(expected_object, result_list[4])

    def testReadSevenEntries_ReturnsCorrectThirdEntry(self):
        third_desc = 'Paul Morphy vs Duke Isouard, Paris, 1858'
        third_fen = '4kb1r/p2n1ppp/4q3/4p1B1/4P3/1Q6/PPP2PPP/2KR4 w k - 1 0'
        third_solution = '1. Qb8+ Nxb8 2. Rd8#'
        expected_object = ChessPuzzle(description=third_desc, fen=third_fen, solution=third_solution)
        result_list = self.importer.parse_file_for_chess_entries('Test_Resources/m8n2.txt')
        self.assertEqual(expected_object, result_list[2])

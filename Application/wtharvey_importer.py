__author__ = 'dimitris'

from Application.models import ChessPuzzle
import string

class WTHarveyImporter:
    def __init__(self):
        pass

    def import_from_file(self, filename):
        obj_list = list()
        game_file = open(filename, 'r')
        line = game_file.next()
        try:
            while line:
                if not self.line_is_whitespace(line):
                    desc = line.rstrip()
                    fen = game_file.next().rstrip()
                    solution = game_file.next().rstrip()
                    obj_list.append(ChessPuzzle(description=desc, fen=fen, solution=solution))
                line = game_file.next()
        except StopIteration:
            pass
        return obj_list

    def line_is_whitespace(self, line):
        return all(c in string.whitespace for c in line)
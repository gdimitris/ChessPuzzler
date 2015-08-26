__author__ = 'dimitris'

from Application.models import ChessPuzzle


class WTHarveyFactory():

    def __init__(self):
        pass

    def create_object_from_entry(self, entry_list):
        description = entry_list.pop(0)
        fen = entry_list.pop(0)
        solution = entry_list.pop(0)
        return ChessPuzzle(description=description, fen=fen, solution=solution)
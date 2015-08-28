__author__ = 'dimitris'

import os
import glob

from Application.models import PuzzleType
from Application import db
from Application.chess_game_importer import ChessGameParser


def populate_db():
    populate_puzzle_types()
    populate_puzzles()


def populate_puzzle_types():
    descriptions = ['Mate in 2', 'Mate in 3', 'Mate in 4']
    for current_desc in descriptions:
        db.session.add(PuzzleType(description=current_desc))
    db.session.commit()


def populate_puzzles():
    os.chdir('../Resources/')
    puzzle_files = glob.glob("*.txt")
    current_puzzle_id = 1
    for puzzle_file in puzzle_files:
        parser = ChessGameParser()
        object_list = parser.parse_file_for_chess_entries(puzzle_file)
        add_object_list_in_db(object_list, current_puzzle_id)
        print "Imported %s puzzles of type_id %d" % (len(object_list), current_puzzle_id)
        current_puzzle_id += 1


def add_object_list_in_db(object_list, puzzle_type_id):
    for game in object_list:
        game.type_id = puzzle_type_id
        db.session.add(game)
    db.session.commit()


if __name__ == '__main__':
    db.create_all()
    populate_db()


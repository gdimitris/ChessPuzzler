__author__ = 'dimitris'

from Application import db

class ChessPuzzle(db.Model):
    __tablename__ = 'Puzzles'

    puzzle_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))
    fen = db.Column(db.String(250), nullable=False)
    solution = db.Column(db.String(250), nullable=False)
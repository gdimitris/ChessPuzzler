__author__ = 'dimitris'

from Application import db


class ChessPuzzle(db.Model):
    __tablename__ = 'Puzzles'

    puzzle_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(200))
    fen = db.Column(db.String(250), nullable=False)
    solution = db.Column(db.String(250), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('PuzzleTypes.type_id'))

    def __eq__(self, other):
        eq_puzzle_id = self.puzzle_id == other.puzzle_id
        eq_description = self.description == other.description
        eq_fen = self.fen == other.fen
        eq_solution = self.solution == other.solution
        eq_type = self.type_id == other.type_id

        return eq_puzzle_id and eq_description and eq_fen and eq_solution and eq_type

    def __str__(self):
        return " id: %s\n descr: %s\n fen: %s\n solution: %s\n type_id: %s\n\n" \
               % (self.puzzle_id, self.description, self.fen, self.solution, self.type_id)


class PuzzleType(db.Model):
    __tablename__ = 'PuzzleTypes'

    type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(100), nullable=False)

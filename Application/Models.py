__author__ = 'dimitris'

from Application import db

class ChessPuzzle(db.Model):
    __tablename__ = 'Puzzles'

    puzzle_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))
    fen = db.Column(db.String(250), nullable=False)
    solution = db.Column(db.String(250), nullable=False)

    def __eq__(self, other):
        eq_puzzle_id = self.puzzle_id == other.puzzle_id
        eq_description = self.description == other.description
        eq_fen = self.fen == other.fen
        eq_solution = self.solution == other.solution

        return eq_puzzle_id and eq_description and eq_fen and eq_solution

    def __str__(self):
        return "id: %s\n descr: %s\n fen: %s\n solution: %s\n" \
               % (self.puzzle_id, self.description, self.fen, self.solution)
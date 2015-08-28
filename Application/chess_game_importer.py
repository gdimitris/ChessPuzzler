__author__ = 'dimitris'

import string
import codecs

from Application.importer_states import HasEntryState, NoEntryState
from Application.wtharvey_factory import WTHarveyFactory


def is_whitespace(line):
    return all(c in string.whitespace for c in line)


class ChessGameParser:
    def __init__(self):
        factory = WTHarveyFactory()
        self.no_entry_state = NoEntryState(self, factory)
        self.entry_state = HasEntryState(self, factory)
        self.current_state = self.no_entry_state

    def get_has_entry_state(self):
        return self.entry_state

    def get_no_entry_state(self):
        return self.no_entry_state

    def set_current_state(self, state):
        self.current_state = state

    def parse_file_for_chess_entries(self, filename):
        chess_game_file = codecs.open(filename, 'r', 'utf-8')
        try:
            self.read_entries(chess_game_file)
        except StopIteration:
            pass

        return self.entry_state.get_object_list()

    def read_entries(self, game_file):
        for line in game_file:
            if is_whitespace(line):
                self.current_state.handle_whitespace_line(line)
            else:
                self.current_state.handle_entry_line(line)


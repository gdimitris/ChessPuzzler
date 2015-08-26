__author__ = 'dimitris'
import abc


class AbstractImporterState:
    __metaclass__ = abc.ABCMeta

    def __init__(self, importer_object, object_factory):
        self.importer_object = importer_object
        self.factory = object_factory

    @abc.abstractmethod
    def handle_whitespace_line(self, line):
        pass

    @abc.abstractmethod
    def handle_entry_line(self, line):
        pass


class NoEntryState(AbstractImporterState):

    def handle_whitespace_line(self, line):
        pass

    def handle_entry_line(self, line):
        entry_state = self.importer_object.get_has_entry_state()
        self.importer_object.set_current_state(entry_state)
        entry_state.handle_entry_line(line)


class HasEntryState(AbstractImporterState):

    def __init__(self, importer_object, object_factory):
        super(HasEntryState, self).__init__(importer_object, object_factory)
        self.entries_buffer_list = list()
        self.object_list = list()

    def handle_entry_line(self, line):
        self.entries_buffer_list.append(line.rstrip())

    def handle_whitespace_line(self, line):
        game_obj = self.factory.create_object_from_entry(self.entries_buffer_list)
        self.object_list.append(game_obj)
        no_entry = self.importer_object.get_no_entry_state()
        self.importer_object.set_current_state(no_entry)

    def get_object_list(self):
        if len(self.entries_buffer_list):
            game_obj = self.factory.create_object_from_entry(self.entries_buffer_list)
            self.object_list.append(game_obj)
        return self.object_list
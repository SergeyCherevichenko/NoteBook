from FileHandlerJson import FileHandlerJson
from MyInterface import MyInterface
from NoteBuilder import NoteBuilder
from Notebook import Notebook


class ServiceNote:

    def __init__(self, my_interface):
        self.notebook = Notebook()
        self.note_builder = NoteBuilder()
        self.my_interface = my_interface

    def add_note(self, title, body, ) -> None:
        note1 = self.note_builder.note_build(title, body)
        self.notebook.add_note(note1)

    def get_notes(self) -> list:
        return self.notebook.get_notes()

    def set_notebook(self)->object:
        return Notebook()



    def remove_notes(self) -> None:
        self.notebook.remove_note()

    def change_note(self) -> None:
        self.notebook.change_note()

    def save(self):
        self.notebook.save()

    def read(self) -> object:
        self.notebook = self.notebook.read()
        service = ServiceNote(FileHandlerJson())
        return service

    def to_string(self) ->None:
        self.notebook.to_string()

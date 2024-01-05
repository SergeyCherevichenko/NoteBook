import datetime

from home_work_notebook.home_work_model.home_work_filehandler.FileHandlerJson import FileHandlerJson
from home_work_notebook.home_work_model.home_work_service_note.home_work_note.Note import Note
from home_work_notebook.home_work_model.home_work_service_note.NoteBuilder import NoteBuilder
from home_work_notebook.home_work_model.home_work_service_note.home_work_notebook.Notebook import Notebook


class ServiceNote:

    def __init__(self, my_interface):
        self.notebook1 = Notebook()
        self.note_builder = NoteBuilder()
        self.my_interface = my_interface

    def add_note(self, title, body, ) -> None:
        note1 = self.note_builder.note_build(title, body)
        self.notebook1.add_note(note1)

    def get_notes(self) -> list:
        return self.notebook1.get_notes()

    def set_notebook1(self, list1):
        note1 = Notebook()
        note1.set_notes(list1)
        self.notebook1 = note1

    def remove_notes(self) -> None:
        self.notebook1.remove_note()

    def change_note(self) -> None:
        self.notebook1.change_note()

    def note_print_by_id(self):
        self.notebook1.print_note_by_id()

    def note_sort_by_data_creating(self):
        self.notebook1.sort_by_data_creating()

    def note_sort_by_data_change(self):
        self.notebook1.sort_by_data_change()

    def save(self):
        self.my_interface.save(self.notebook1.get_notes())

    def read(self) -> object:
        json_python = self.my_interface.read()
        note_list = []
        for i in json_python:
            my_dict = dict(i)
            id1 = my_dict.get("Заметка №")
            title = my_dict.get("Заголовок")
            body = my_dict.get("Содержание")
            creating = my_dict.get("Дата создания")
            data_creating = datetime.datetime.strptime(creating, "%Y/%m/%d %H-%M-%S")
            change = my_dict.get("Дата изменения")
            data_change = datetime.datetime.strptime(change, "%Y/%m/%d %H-%M-%S")
            note = Note(title, body)
            note.set_note_id(id1)
            note.set_note_data_change(data_change)
            note.set_note_data_creating(data_creating)
            note_list.append(note)
        service = ServiceNote(FileHandlerJson())
        self.set_notebook1(note_list)
        service.note_builder = NoteBuilder()
        Note.id = len(note_list) + 1
        return service

    def to_string(self):
        self.notebook1.to_string()

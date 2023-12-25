import datetime
import json

from FileHandlerJson import FileHandlerJson


class Note:
    id = 1

    def __init__(self, title, body):
        self.id = Note.id
        self.__title = title
        self.__body = body
        self.data_creation = datetime.datetime.now()
        self.data_change = datetime.datetime.now()
        Note.id += 1

    def dump(self) -> dict:
        dt_note = {"Заметка №": self.id, "Заголовок": self.__title, "Содержание": self.__body,
                   "Дата создания": self.data_creation.strftime("%Y/%m/%d  %H-%M-%S"),
                   "Дата изменения": self.data_change.strftime("%Y/%m/%d  %H-%M-%S")}
        return dt_note

    def get_note_id(self) -> int:
        return self.id

    def get_note_title(self) -> str:
        return self.__title

    def get_note_body(self) -> str:
        return self.__body

    def get_note_data_creating(self) -> datetime:
        return self.data_creation

    def get_note_data_creating_str(self) -> str:
        return self.data_creation.strftime("%Y/%m/%d  %H-%M-%S")

    def get_note_data_change_str(self) -> str:
        return self.data_change.strftime("%Y/%m/%d  %H-%M-%S")

    def get_note_data_change(self) -> datetime:
        return self.data_change

    def set_note_title(self, title) -> None:
        self.__title = title
        self.data_change = datetime.datetime.now()

    def set_note_body(self, body):
        self.__body = body
        self.data_change = datetime.datetime.now()

    def note_to_string(self):
        data_creating_str = self.data_creation.strftime("%Y/%m/%d  %H-%M-%S")
        data_change_str = self.data_change.strftime("%Y/%m/%d  %H-%M-%S")
        return (f"Заметка №{self.id}\n\nЗаголовок - {self.__title}\n\nСодержание - {self.__body}"
                f"\n\nДата создания  :   {self.get_note_data_creating_str()}"
                f"\nДата изменения :   {self.get_note_data_change_str()}\n"
                f"--------------------------------\n")

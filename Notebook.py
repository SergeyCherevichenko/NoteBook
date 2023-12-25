import json
from tkinter.ttk import Notebook

from FileHandlerJson import FileHandlerJson
from Note import Note



class Notebook:

    def __init__(self):
        self.notes = []

    def get_notes(self) -> list:
        return self.notes

    def set_notes(self,list):
        self.notes = list

    def dump(self):
        return {"Заметки":{"Заметка №": Note.get_note_id(),"Заголовок": Note.set_note_title(),
                            "Содержание": Note.set_note_body(),
                            "Дата создания": Note.get_note_data_creating_str(),
                            "Дата изменения": Note.get_note_data_change_str()}}




    def add_note(self, note):
        self.notes.append(note)

    def remove_note(self) -> None:
        number_note = int(input("Введите номер заметки которую вы хотите удалить: "))
        flag = False
        for i in self.notes:
            if i.get_note_id() == number_note:
                self.notes.remove(i)
                flag = True
        if flag:
            print("Заметка успешно удалена!\n-----------------------\n")
        else:
            print("Заметки с таким номером нет в вашем списке!\n-------------------\n")

    def change_note(self) -> None:
        number_note = int(input("Введите номер заметки которую вы хотите изменить: "))
        flag = False
        for i in self.notes:
            if i.get_note_id() == number_note:
                while (not flag):
                    op = int(
                        input("Заметка найдена, что вы хотите изменить Заголовок или Содержание. Нажмите 1 или 2: "))
                    if op == 1:
                        new_title = input("Введите новый заголовок: ")
                        i.set_note_title(new_title)
                        print("Заголовок заметки изменен!")
                        flag = True
                    elif op == 2:
                        new_body = input("Введите новое содержание: ")
                        i.set_note_body(new_body)
                        print("Содержание заметки изменено!")
                        flag = True
                    else:
                        print("Вы ввели не верную операцию! Попробуйте еще раз!")

        if not flag: print("Заметки с таким номером не существует!\n------------------------------")

    def save(self):
        filehandler = FileHandlerJson()
        filehandler.save(self.notes)

    def read(self):
        fileHandler = FileHandlerJson()
        noty = fileHandler.read()
        self.set_notes(noty)






    def to_string(self):
        for i in self.notes:
            print(i.note_to_string())

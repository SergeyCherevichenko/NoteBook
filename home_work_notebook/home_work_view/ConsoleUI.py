from home_work_notebook.home_work_presenter.Presenter import Presenter
from home_work_notebook.home_work_view.View import View
from home_work_notebook.home_work_view.home_work_command.MainMenu import MainMenu


class ConsoleUI(View):

    def __init__(self):
        self.presenter = Presenter(self)
        self.work = True
        self.menu = MainMenu(self)

    def print_answer(self, answer) -> None:
        pass

    def start(self) -> None:
        print("Здравствуйте. Вас приветствует программа \"Заметки\" версии 1.0")
        while(self.work):
            self.print_menu()
            self.choice()

    def choice(self)->None:
        line = int(input("Выберите одну из операций ниже по номеру: "))
        if 0 < line <= self.menu.size():
            self.menu.execute(line)
        else:
            self.error()

    def error(self)->None:
        print("Операции с таким номером не существует! Выберите из списка.")

    def print_menu(self):
        print(self.menu.menu())

    def finish(self):
        print("До новых встреч!")
        self.work = False

    def add_note(self):
        title = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        self.presenter.add_note(title,body)

    def all_print_note(self):
        self.presenter.all_print_note()

    def change_note(self):
        self.presenter.change_note()

    def note_print_by_id(self):
        self.presenter.note_print_by_id()

    def note_sort_by_data_creating(self):
        self.presenter.sort_note_by_data_creating()

    def note_sort_by_data_change(self):
        self.presenter.sort_note_by_data_change()

    def read_note(self):
        self.presenter.note_read()

    def note_save(self):
        self.presenter.note_save()

    def remove_note(self):
        self.presenter.remove_note()






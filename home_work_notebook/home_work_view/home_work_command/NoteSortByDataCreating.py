from home_work_notebook.home_work_view.home_work_command.Command import Command


class NoteSortByDataCreating(Command):

    def __init__(self, consoleUI):
        self.consoleUI = consoleUI
        super().__init__("Сортировать заметки по дате создания",self.consoleUI)

    def execute(self) -> None:
        self.consoleUI.note_sort_by_data_creating()
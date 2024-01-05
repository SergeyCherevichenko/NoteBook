from home_work_notebook.home_work_view.home_work_command.Command import Command


class NoteSortByDataChange(Command):

    def __init__(self, consoleUI):
        self.consoleUI = consoleUI
        super().__init__("Сортировать заметки по дате изменения",self.consoleUI)
    def execute(self) -> None:
        self.consoleUI.note_sort_by_data_change()
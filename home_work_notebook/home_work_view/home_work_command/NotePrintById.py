from home_work_notebook.home_work_view.home_work_command.Command import Command


class NotePrintById(Command):

    def __init__(self, consoleUI):
        self.consoleUI = consoleUI
        super().__init__("Вывести на экран заметку по номеру", self.consoleUI)

    def execute(self) -> None:
        self.consoleUI.note_print_by_id()

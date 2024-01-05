from home_work_notebook.home_work_view.home_work_command.Command import Command


class AllPrintNote(Command):

    def __init__(self,consoleUI):
        self.consoleUI = consoleUI
        super().__init__("Вывести на экран все заметки",self.consoleUI)

    def execute(self) -> None:
        self.consoleUI.all_print_note()
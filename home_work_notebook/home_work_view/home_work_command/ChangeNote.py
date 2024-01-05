
from home_work_notebook.home_work_view.home_work_command.Command import Command


class ChangeNote(Command):

    def __init__(self, consoleUI):
        self.consoleUI = consoleUI
        super().__init__("Изменить заметку", self.consoleUI)

    def execute(self) -> None:
        self.consoleUI.change_note()

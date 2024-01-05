
from home_work_notebook.home_work_view.home_work_command.Command import Command


class AddNote(Command):

    def __init__(self,consoleUI):
        self.consoleUI = consoleUI
        super().__init__("Добавить заметку", consoleUI=self.consoleUI)


    def execute(self) -> None:
        self.consoleUI.add_note()

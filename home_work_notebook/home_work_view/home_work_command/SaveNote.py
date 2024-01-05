from home_work_notebook.home_work_view.home_work_command.Command import Command


class SaveNote(Command):

    def __init__(self, consoleUI):
        self.consoleUI = consoleUI
        super().__init__("Сохранить список заметок",self.consoleUI)

    def execute(self) -> None:
        self.consoleUI.note_save()
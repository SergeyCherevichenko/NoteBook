from home_work_notebook.home_work_view.home_work_command.Command import Command


class ReadNote(Command):

    def __init__(self, consoleUI):
        self.consoleUI = consoleUI
        super().__init__("Востанить список заметок из сохранненого файла",self.consoleUI)
    def execute(self) -> None:
        self.consoleUI.read_note()
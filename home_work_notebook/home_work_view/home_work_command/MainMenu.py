
from home_work_notebook.home_work_view.home_work_command.AddNote import AddNote
from home_work_notebook.home_work_view.home_work_command.AllPrintNote import AllPrintNote
from home_work_notebook.home_work_view.home_work_command.ChangeNote import ChangeNote
from home_work_notebook.home_work_view.home_work_command.Finish import Finish

from home_work_notebook.home_work_view.home_work_command.NotePrintById import NotePrintById
from home_work_notebook.home_work_view.home_work_command.NoteSortByDataChange import NoteSortByDataChange
from home_work_notebook.home_work_view.home_work_command.NoteSortByDataCreating import NoteSortByDataCreating
from home_work_notebook.home_work_view.home_work_command.ReadNote import ReadNote
from home_work_notebook.home_work_view.home_work_command.RemoveNote import RemoveNote
from home_work_notebook.home_work_view.home_work_command.SaveNote import SaveNote


class MainMenu:

    def __init__(self,consoleUI):
        self.command = []
        self.command.append(AddNote(consoleUI))
        self.command.append(ChangeNote(consoleUI))
        self.command.append(RemoveNote(consoleUI))
        self.command.append(NotePrintById(consoleUI))
        self.command.append(NoteSortByDataCreating(consoleUI))
        self.command.append(NoteSortByDataChange(consoleUI))
        self.command.append(AllPrintNote(consoleUI))
        self.command.append(ReadNote(consoleUI))
        self.command.append(SaveNote(consoleUI))
        self.command.append(Finish(consoleUI))

    def menu(self):
        st = ""
        for i in range(len(self.command)):
            st = str(st) + str(i+1) + " " + self.command[i].get_discription() + "\n"

        return st


    def execute(self, choice) -> None:
        commands = self.command[choice - 1]
        commands.execute()

    def size(self) -> int:
        return len(self.command)

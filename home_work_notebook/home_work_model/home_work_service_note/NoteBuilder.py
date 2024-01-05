

from home_work_notebook.home_work_model.home_work_service_note.home_work_note.Note import Note
class NoteBuilder:
    def note_build(self, title, body) -> Note:
        note = Note(title, body)
        return note

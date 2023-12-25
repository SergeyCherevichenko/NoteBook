

from Note import Note


class NoteBuilder:
    def note_build(self, title, body) -> Note:
        note = Note(title, body)
        return note

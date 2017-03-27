from django.test import TestCase

from notes.models import Note


class NotesModelTest(TestCase):
    """Test Note Model"""

    def test_str(self):
        note = Note.objects.create(text="Buy bread, pasta, oranges.")
        note1 = Note.objects.create(text="Buy bread")
        note2 = Note.objects.create(text="Buy")
        note3 = Note.objects.create(text="")

        self.assertEqual(str(note), "Buy bread, ...")
        self.assertEqual(str(note1), "Buy bread")
        self.assertEqual(str(note2), "Buy")
        self.assertEqual(str(note3), "")

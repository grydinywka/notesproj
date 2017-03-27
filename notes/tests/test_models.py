from django.test import TestCase

from notes.models import Note, Book


class ModelsTest(TestCase):
    """Test for Models"""

    def test_str_note(self):
        note = Note.objects.create(text="Buy bread, pasta, oranges.")
        note1 = Note.objects.create(text="Buy bread")
        note2 = Note.objects.create(text="Buy")
        note3 = Note.objects.create(text="")

        self.assertEqual(str(note), "Buy bread, ...")
        self.assertEqual(str(note1), "Buy bread")
        self.assertEqual(str(note2), "Buy")
        self.assertEqual(str(note3), "")

    def test_book(self):
        note1 = Note.objects.create(text="Buy bread")
        note2 = Note.objects.create(text="Buy")
        book = Book.objects.create()

        book.notes.add(note1)
        book.notes.add(note2)

        self.assertIn(note1, book.notes.all())
        self.assertIn(note2, book.notes.all())

    def test_book_drop_notes(self):
        book_count = Book.objects.count()
        note1 = Note.objects.create(text="Buy bread")
        note2 = Note.objects.create(text="Buy")
        book = Book.objects.create()

        book.notes.add(note1)
        book.notes.add(note2)

        book.notes.remove(note1)
        book.notes.remove(note2)

        self.assertEqual(book_count, Book.objects.count())

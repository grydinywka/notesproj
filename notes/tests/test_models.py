from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from notes.models import Note, Book, RequestMy


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
        book = Book.objects.create(name="rest")
        #
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

    def test_request(self):
        client = Client()
        url = reverse('home')
        response = client.get(url)
        requests_count = RequestMy.objects.count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, requests_count)

        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, requests_count)

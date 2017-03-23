from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from notes.models import Note


class TestNoteAddForm(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('notes_add')

    def test_form(self):
        # get response
        response = self.client.get(self.url)

        # check response status
        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Text', response.content)
        self.assertIn(b'name="add_button"', response.content)
        self.assertIn(b'name="cancel_button"', response.content)
        self.assertIn('action="%s"' % self.url, response.content.decode())

    def test_success(self):
        response = self.client.post(self.url, {
            'text': "Field Text filed"
            }, follow=True
        )

        self.assertEqual(response.status_code, 200)
        note = Note.objects.get(pk=6)
        self.assertEqual(note.text, "Field Text filed")
        self.assertIn(b'Note create successfully', response.content)

        self.assertEqual(response.redirect_chain[0][0], '/')

    def test_cancel(self):
        value_notes = Note.objects.all().count()
        response = self.client.post(self.url, {
            'text': "Field Text filed",
            'cancel_button': True
            }, follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Note is not create", response.content)

        self.assertEqual(response.redirect_chain[0][0], '/')
        self.assertEqual(value_notes, Note.objects.all().count())

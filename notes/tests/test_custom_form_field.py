from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from notes.models import Note
from notes.forms import MIN_LEN_NOTE


class TestNoteAddFormCustomField(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_form(self):
        # get response
        response = self.client.get(self.url, {
            "add_note_link": True
        }, follow=False)

        # check response status
        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Text', response.content)
        self.assertIn(b'name="add_button"', response.content)
        self.assertIn(b'name="cancel_button"', response.content)
        self.assertIn('action="%s"' % self.url, response.content.decode())

    def test_success(self):
        response = self.client.post(self.url, {
            'text': "Field Text filed",
            'add_button': True
            }, follow=False
        )

        self.assertEqual(response.status_code, 200)
        note = Note.objects.get(pk=6)
        self.assertEqual(note.text, "FIELD TEXT FILED")
        self.assertIn(b'Note uppercase create successfully', response.content)

    def test_cancel(self):
        value_notes = Note.objects.all().count()
        response = self.client.post(self.url, {
            'text': "Field",
            'cancel_button': True
            }, follow=False
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Note uppercase is not create", response.content)

        self.assertEqual(value_notes, Note.objects.all().count())

    def test_less_ten_char(self):
        value_notes = Note.objects.all().count()
        response = self.client.post(self.url, {
            'text': "Field",
            'add_button': True
            }, follow=False
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('The text field required at least {} characters'.
                      format(MIN_LEN_NOTE), response.content.decode())

        self.assertEqual(value_notes, Note.objects.all().count())

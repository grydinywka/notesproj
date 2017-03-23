from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.template import Template, Context

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
        self.assertIn(b'action="%s"' % self.url, response.content)

    def test_success(self):
        response = self.client.post(self.url, {
            'text': "Field Text filed"
            }, follow=True
        )

        self.assertExual(response.status_code, 200)
        note = Note.objects.get(pk=1)
        self.assertEqual(note.text, "Field Text filed")
        self.assertIn(b'Note create successfully', response.content)

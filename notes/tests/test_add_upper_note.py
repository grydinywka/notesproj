from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from notes.models import Note
from notes.forms import MIN_LEN_NOTE


class TestNoteAddFormCustomField(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('notes_add_upper')

    def test_form(self):
        # get response
        response = self.client.get(self.url, {}, follow=True,
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                   )

        # check response status
        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Text', response.content)
        self.assertIn(b'name="add_button"', response.content)
        self.assertIn(b'name="cancel_button"', response.content)
        self.assertIn('action="%s"' % self.url, response.content.decode())

    def test_success(self):
        # make post-ajax request
        response = self.client.post(self.url, {
            'text': "Field Text filed",
            'add_button': True
            }, follow=True,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )

        self.assertEqual(response.status_code, 200)
        note = Note.objects.get(pk=6)
        self.assertEqual(note.text, "FIELD TEXT FILED")
        self.assertIn(b'Note uppercase create successfully', response.content)

        self.assertEqual(response.redirect_chain[0][0], '/')

    def test_empty(self):
        value_notes = Note.objects.all().count()
        response = self.client.post(self.url, {
            'text': "",
            'add_button': True
            }, follow=True,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"This field is required.", response.content)

        self.assertEqual(value_notes, Note.objects.count())

    def test_less_ten_char(self):
        value_notes = Note.objects.all().count()
        response = self.client.post(self.url, {
            'text': "Field",
            'add_button': True
            }, follow=True,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('The text field required at least {} characters'.
                      format(MIN_LEN_NOTE), response.content.decode())

        self.assertEqual(value_notes, Note.objects.count())

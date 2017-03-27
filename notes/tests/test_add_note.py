from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from notes_proj.settings import STATICFILES_DIRS

from notes.models import Note
from notes.forms import MIN_LEN_NOTE


class NoteAddFormTest(TestCase):
    """
    The Test class for form of creating new note
    """
    fixtures = ['init_notes']

    def setUp(self):
        self.client = Client()
        self.url = reverse('notes_add')

    def test_form(self):
        response = self.client.get(
            self.url,
            follow=True,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )

        # check response status
        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Text', response.content)
        self.assertIn(b'Note-image', response.content)
        self.assertIn(b'name="add_button"', response.content)
        self.assertIn(b'name="cancel_button"', response.content)
        self.assertIn('action="%s"' % self.url, response.content.decode())

    def test_success(self):
        i = STATICFILES_DIRS[0] + '/img/DSC_0000098.jpg'
        img = open(i, 'rb')
        uploaded = SimpleUploadedFile(img.name, img.read())
        response = self.client.post(
            self.url,
            {'text': "Field Text filed", "image": uploaded},
            follow=True,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )

        self.assertEqual(response.status_code, 200)
        note = Note.objects.get(pk=6)
        self.assertEqual(note.text, "FIELD TEXT FILED")
        self.assertEqual(note.image is not None, True)
        self.assertEqual('created', response.json()['status'])
        self.assertEqual(note.id, response.json()['note_id'])

    def test_empty(self):
        value_notes = Note.objects.count()
        response = self.client.post(
            self.url,
            follow=True,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual('errors', response.json()['status'])
        self.assertIn("This field is required.",
                      response.json()['errors']['text'])
        self.assertEqual({}, response.json()['data'])
        self.assertEqual(value_notes, Note.objects.count())

    def test_less_ten_char(self):
        value_notes = Note.objects.count()
        response = self.client.post(
            self.url,
            {'text': "Field"},
            follow=True,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual('errors', response.json()['status'])
        self.assertIn('The text field required at least {} characters'.
                      format(MIN_LEN_NOTE), response.json()['errors']['text'])
        self.assertEqual("Field", response.json()['data']['text'])
        self.assertEqual(value_notes, Note.objects.all().count())

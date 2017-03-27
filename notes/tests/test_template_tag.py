from django.test import TestCase
from django.template import Template, Context

from notes.models import Note


class TemplateTagTest(TestCase):
    """
    Test template tag
    """

    def setUp(self):
        # create notes objects
        Note.objects.create(text="Buy pasta and tomatoes")
        Note.objects.create(text="Call to husband")
        Note.objects.create(text="Empty trash")
        Note.objects.create(text="My boats is ")

    def test_id2note(self):
        # test id2note template tag
        note = Note.objects.get(text="Empty trash")

        out_note = Template(
            "{% load id2note %}"
            "{% id2note id %}"
        ).render(Context({"id": note.id}))

        self.assertTrue(note, out_note)

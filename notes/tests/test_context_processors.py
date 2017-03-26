from django.test import TestCase
from django.http import HttpRequest

from notes.context_processors import count_notes_processor
from notes.models import Note


class ContextProcessorsTest(TestCase):
    """
    Test for context processors
    """
    fixtures = ['init_notes']

    def test_count_notes_processor(self):
        request = HttpRequest()
        data = count_notes_processor(request)

        # now we have 5 notes - from fixture
        count = Note.objects.count()
        self.assertEqual(data['NOTE_COUNT'], count)

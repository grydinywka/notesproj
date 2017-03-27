from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class WidgetTest(TestCase):
    """
    The Test class for checking widget
    which generate html with random note object.
    """
    fixtures = ['init_notes']

    def setUp(self):
        self.client = Client()
        self.url = reverse('note_random')

    def test_widget(self):
        response = self.client.get(
            self.url,
        )

        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Random note object is:', response.content)
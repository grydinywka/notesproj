from __future__ import unicode_literals

from django.db import models


class Note(models.Model):
    """ Model for Notes """
    text = models.TextField()

    def __str__(self):
        length = len(self.text.split())
        if length > 2:
            return " ".join(self.text.split()[:2]) + " ..."
        else:
            return self.text

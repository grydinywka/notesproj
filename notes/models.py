from __future__ import unicode_literals

from django.db import models


class Note(models.Model):
    """ Model for Notes """
    text = models.TextField()
    image = models.ImageField(
        upload_to="note_images/",
        blank=True,
        null=True,
        verbose_name='Note-image'
    )

    def __str__(self):
        length = len(self.text.split())
        if length > 2:
            return " ".join(self.text.split()[:2]) + " ..."
        else:
            return self.text


class Book(models.Model):
    """
    The model for storing notes
    """
    name = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        default=None
    )
    notes = models.ManyToManyField(
        Note,
        blank=True,
        default=None
    )

    def get_notes(self):
        notes = [note.__str__() for note in self.notes.all()]
        return notes

    def __str__(self):
        return self.name


class RequestMy(models.Model):
    """Model for storing requests"""

    path = models.CharField(max_length=255)
    method = models.CharField(max_length=63)

    def __str__(self):
        return "Request {} {}".format(self.method, self.path)

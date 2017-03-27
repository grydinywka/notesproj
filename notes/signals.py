from django.db.models.signals import post_delete, m2m_changed
from django.dispatch import receiver

from notes.models import Note, Book


@receiver(post_delete, sender=Note)
def post_drop_note(sender, **kwargs):
    """
    After delete Note we will check if there are books with empty list note
    and drop them
    """
    books = Book.objects.filter(notes=None)
    for book in books:
        book.delete()


@receiver(m2m_changed, sender=Book.notes.through)
def m2m_book(sender, **kwargs):
    """
    After change notes in book we check if book has any note
    If notes is empty - drop Book
    """

    book = kwargs['instance']
    if kwargs['action'] == 'post_remove':
        try:
            if book.notes.count() == 0:
                book.delete()
        except ValueError:
            pass

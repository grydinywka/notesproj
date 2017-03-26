from notes.models import Note


def count_notes_processor(request):
    return {"NOTE_COUNT": Note.objects.count()}

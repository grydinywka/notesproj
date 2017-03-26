from django import template
from notes.models import Note

register = template.Library()


@register.simple_tag
def id2note(note_id, *args):
    try:
        note = Note.objects.get(pk=note_id)
    except (Note.DoesNotExist, ValueError):
        note = None
    t = template.Template("{{ note }}")
    return t.render(template.Context({"note": note}))

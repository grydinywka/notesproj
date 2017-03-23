from django import template
from notes.models import Note

register = template.Library()


@register.tag
def id2note(parser, token):
    try:
        tag_name, note_id = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("{} tag requires 1 argument".\
                                           format(token.contents.split()[0]))

    return NoteIdNode(note_id)


class NoteIdNode(template.Node):
    def __init__(self, note_id):
        self.note_id = template.Variable(note_id)

    def render(self, context):
        try:
            note = Note.objects.get(pk=self.note_id.resolve(context))
        except Exception:
            note = None
        t = template.Template("{{ note }}")
        return t.render(template.Context({"note": note}))
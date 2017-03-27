from django.views.generic import ListView, CreateView, TemplateView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from notes.models import Note
from notes.forms import CreateNoteUpperForm


class NoteListView(ListView):
    """
    The view for render list of notes
    """
    model = Note
    context_object_name = "notes"


class NoteCreateView(CreateView):
    """
    The view for creating new uppercase note objects.
    If user make POST - response will JSON.
    If GET - html template with form.
    Make post may do from other domains
    """
    template_name = "notes/note_form.html"
    model = Note
    form_class = CreateNoteUpperForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # print(form.cleaned_data)
        note = Note.objects.create(text=form.cleaned_data['text'],
                                   image=form.cleaned_data['image'])
        new_count = Note.objects.count()
        return JsonResponse({"status": "created", "note_id": note.id,
                             "new_count": new_count})

    def form_invalid(self, form):
        errors = {}
        for field, errs in form.errors.items():
            errors[field] = errs
        return JsonResponse({"status": "errors", "errors": errors,
                             "data": form.data})


class NoteRandomView(TemplateView):
    template_name = 'notes/note_random.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        note = Note.objects.order_by('?')[0]
        context['note'] = note.text

        return context

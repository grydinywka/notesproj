from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from notes.models import Note
from notes.forms import CreateNoteUpperForm


class NoteListView(ListView):
    model = Note
    context_object_name = "notes"


class NoteUpperCreateView(CreateView):
    template_name = "notes/note_upper_form.html"
    model = Note
    form_class = CreateNoteUpperForm

    def get_success_url(self):
        messages.success(self.request, "Note uppercase create successfully")
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            return super(NoteUpperCreateView, self).post(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('home'))

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return super(NoteUpperCreateView, self).get(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('home'))
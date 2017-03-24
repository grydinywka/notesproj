from django.views.generic import ListView, CreateView, FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from notes.models import Note
from notes.forms import CreateNoteForm


class NoteListView(ListView):
    model = Note
    context_object_name = "notes"


class NoteCreateView(CreateView):
    model = Note
    form_class = CreateNoteForm

    def get_success_url(self):
        messages.success(self.request, "Note create successfully")
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get("cancel_button"):
            messages.success(self.request, "Note is not create")
            return HttpResponseRedirect(reverse('home'))
        return super(NoteCreateView, self).post(request, *args, **kwargs)
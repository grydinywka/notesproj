from django.shortcuts import render
from django.views.generic import ListView

from notes.models import Note


class NoteListView(ListView):
    model = Note
    context_object_name = "notes"



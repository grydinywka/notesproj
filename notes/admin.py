from django.contrib import admin
from django.forms import ModelForm, ValidationError, Textarea

from notes.models import Note
from notes.forms import CharFieldUpper


class NoteFormAdmin(ModelForm):
    text = CharFieldUpper(
        widget=Textarea(attrs={
            'class': 'form-control',
            'cols': 80
        })
    )

class NoteAdmin(admin.ModelAdmin):
    form = NoteFormAdmin

admin.site.register(Note, NoteAdmin)

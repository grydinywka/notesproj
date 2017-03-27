from django.contrib import admin
from django.forms import ModelForm, Textarea

from notes.models import Note, Book, RequestMy
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


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_notes']

admin.site.register(Note, NoteAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(RequestMy)

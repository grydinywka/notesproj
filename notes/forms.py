from django import forms
from django.core.exceptions import ValidationError
from notes.models import Note

MIN_LEN_NOTE = 10


class CreateNoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('text',)

    def clean_text(self):
        data = self.cleaned_data['text']
        if len(data) < MIN_LEN_NOTE:
                raise ValidationError('The text field required at least {} characters'.format(MIN_LEN_NOTE))
        return data

from django import forms
from django.core.exceptions import ValidationError
from notes.models import Note

MIN_LEN_NOTE = 10


class CreateNoteForm(forms.ModelForm):
    """
    The form for creating simple note object.
    We check note's length. It must be more than 9.
    """
    error_css_class = 'text-danger has-error'
    required_css_class = "required"

    class Meta:
        model = Note
        fields = ('text', 'image')

    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control'})
    )

    def clean_text(self):
        data = self.cleaned_data['text']
        if len(data) < MIN_LEN_NOTE:
            raise ValidationError('The text field required at least'
                                  ' {} characters'.format(MIN_LEN_NOTE))
        return data


class CharFieldUpper(forms.CharField):
    """
    The custom field for making uppercase note
    """
    def to_python(self, value):
        value = super().to_python(value)

        return value.upper()


class CreateNoteUpperForm(CreateNoteForm):
    """
    The form for creating note object which will have
    only uppercase letters.
    We check note's length. It must be more than 9.
    """
    text = CharFieldUpper(
        widget=forms.Textarea(attrs={
            'class': 'form-control'})
    )

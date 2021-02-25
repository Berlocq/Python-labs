from django import forms
from . import models


class AuthorForm(forms.ModelForm):
    class Meta:
        model=models.Author
        fields=('name', 'book_name')

class GenreForm(forms.ModelForm):
    class Meta:
        model=models.Genre
        fields=('author', 'style', 'description')

class SeriesForm(forms.ModelForm):
    class Meta:
        model=models.Series
        fields=('author', 'number')

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if name == "Pavel":
            self.add_error('name', 'incorrect name')
        return cleaned_data         
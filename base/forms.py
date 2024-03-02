from django import forms

from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.BookModel
        fields = ["genre", "title", "author", "description", "file"]

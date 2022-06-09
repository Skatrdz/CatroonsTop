from django import forms
from .models import *
class TestForm(forms.Form):
    title = forms.CharField(max_length=255, label="Заголовочек")
    slug = forms.SlugField(max_length=255, label="URL")

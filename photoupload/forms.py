from django import forms
from django.forms import ModelForm
from .models import Image

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':
True}))
    year = forms.CharField(max_length = 4)


class ImageInspect(ModelForm):
    class Meta:
        model = Image
        fields = ['caption', 'memories', 'tags']

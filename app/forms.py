from django import forms
from django.forms import ModelForm
from app.models import Post
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class PostModelForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['user']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':''}),
            'limit_datetime': DateTimePickerInput(attrs={'placeholder':'', 'required':False}),
            'description': forms.Textarea(attrs={'placeholder':''}),
        }

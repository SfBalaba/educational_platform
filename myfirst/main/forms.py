from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class FormTask(ModelForm):
    class Meta:
        model = Task
        fields = ["article_type", "title", "task"]
        widgets = {
            "article_type": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название',}),
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название',
            }),
            "task": Textarea(attrs={
                "class" : "form-control",
                "placeholder": "Введите название",
                               }),

        }
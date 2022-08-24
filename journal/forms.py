from django import forms
from django.forms import ModelForm
from .models import Article

class FormArticle(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categ'].empty_label = "Выберите категорию"

    class Meta:
        model = Article # название модели на основе которой создается форма
        fields = [
            'title',
            'text',
            'categ',
        ]

        widgets = {
            'text': forms.Textarea(attrs={'cols':60, 'rows':5})
        }

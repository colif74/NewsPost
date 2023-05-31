from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    header = forms.CharField(min_length=10)

    class Meta:
        model = Post
        fields = [
                'post_tip',
                'category'
                'header',
                'contents',
                'author',
                    ]

    def clean(self):
        cleaned_data = super().clean()
        header = cleaned_data.get('header')
        contents = cleaned_data.get("contents")
        if contents == header:
            raise ValidationError({"Содержание должно отлтчатся от заголовка"})
        return cleaned_data

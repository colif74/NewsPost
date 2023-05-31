from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    header = forms.CharField(max_length=10)

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
            clean_data = super().clean()
            header = clean_data.get('header')
            contents == clean_data.get("contents")
            if contents == header:
                raise ValidationError({"Содержание должно отлтчатся от заголовка"})
            return clean_data

from django import forms
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from .models import Post


class PostForm(forms.ModelForm):
    header = forms.CharField(min_length=10)

    class Meta:
        model = Post
        fields = [
                'post_tip',
                'category',
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


class StateForm(forms.ModelForm):
    header = forms.CharField(min_length=10)

    class Meta:
        model = Post
        fields = [
                'post_tip',
                'category',
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


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )

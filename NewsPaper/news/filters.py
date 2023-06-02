import django_filters
from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
           'header': ['iexact'],
           'author': ['exact'],
           'date_in': ['gt'],
            }

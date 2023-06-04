from django_filters import FilterSet

class ArticleFilter(FilterSet):

    class Meta:
        model = Author
        fields = [...]

    @property
    def qs(self):
        parent = super().qs
        author = getattr(self.request, 'user', None)

        return parent.filter(is_published=True) \
            | parent.filter(author=author)
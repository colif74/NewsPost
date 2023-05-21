from django.views.generic import ListView
from .models import Post, Category

class PostList(ListView):
    model = Post
    ordering = 'name'
    template_name = 'post.html'
    context_object_name = 'post'


class CategoryList(ListView):
    model = Category
    ordering = 'Category'
    template_name = 'category.html'
    context_object_name = 'category'



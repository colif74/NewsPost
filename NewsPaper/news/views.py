from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post, Author, Category



class AuthorList(ListView):
    model = Author
    ordering = 'user'
    template_name = 'author.html'
    context_object_name = 'author'



class AuthorDetail(DetailView):
    model = Author
    template_name = 'author.html'
    context_object_name = 'author'


class PostList(ListView):
    model = Post
    ordering = 'header'
    template_name = 'news.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_id'] = id(Post)
        return context



class PostDetail(DetailView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'



class CategoryList(ListView):
    model = Category
    ordering = 'post_or_news'
    template_name = 'category.html'
    context_object_name = 'category'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'

from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post, Author, Category
from .filters import PostFilter
from forms import PostForm
from django.shortcuts import render



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
    paginate_by = 4

    def get_context_data_1(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['news_id'] = id(Post)
    #     return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'


def create_post(request):
    form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

class CategoryList(ListView):
    model = Category
    ordering = 'post_or_news'
    template_name = 'category.html'
    context_object_name = 'category'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'




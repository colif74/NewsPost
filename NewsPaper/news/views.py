from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Author, Category
from .filters import PostFilter
from .forms import PostForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


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
    paginate_by = 15

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.filterset = None

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

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/news/')

    return render(request, 'post_edit.html', {'form': form})


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class StateUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'state_edit.html'


class StateDelete(DeleteView):
    model = Post
    template_name = 'state_delete.html'
    success_url = reverse_lazy('post_list')


class StateCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'state_edit.html'


class CategoryList(ListView):
    model = Category
    ordering = 'post_or_news'
    template_name = 'category.html'
    context_object_name = 'category'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'

from django.views.generic import ListView, DetailView, CreateView,\
    TemplateView, UpdateView, DeleteView
from .models import Post, Author, Category
from .filters import PostFilter
from .forms import PostForm,  BaseRegisterForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView as AuthLoginView


class LoginView(AuthLoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
        return super().form_valid(form)


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='author').exists()
        return context


class AuthorList(ListView):
    model = Author
    ordering = '-user'
    template_name = 'author.html'
    context_object_name = 'author'
    paginate_by = 10


class AuthorDetail(DetailView):
    model = Author
    template_name = 'author.html'
    context_object_name = 'author'


class PostList(ListView):
    model = Post
    ordering = '-date_in'
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 15

    # def __init__(self, **kwargs):
    #     super().__init__(kwargs)
    #     self.filterset = None

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
            return HttpResponseRedirect('news/')

    return render(request, 'post_edit.html', {'form': form})


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        new = form.save(commit=False)
        if self.request.path == '/news/create/':
            new.post_tip_id = 1
        elif self.request.path == '/state/create/':
            new.post_tip_id = 2
            new.save()
        return super().form_valid(form)


class StateCreateView(PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'state_edit.html'
    permission_required = ('news.create_post',)
    form_class = PostForm
    success_url = 'news/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_tip = 'ST'
        return super().form_valid(form)


class StateUpdateView(PermissionRequiredMixin, UpdateView):
    model = Post
    template_name = 'state_edit.html'
    permission_required = ('news.update_post',)
    form_class = PostForm
    success_url = 'news/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_tip = 'ST'
        return super().form_valid(form)


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.update_post',)
    form_class = PostForm
    success_url = 'news/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_tip = 'NW'
        return super().form_valid(form)


class PostCreateView(PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.create_post',)
    form_class = PostForm
    success_url = 'news/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_tip = 'NW'
        return super().form_valid(form)


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'state_delete.html'
    permission_required = ('news.delete_post',)
    form_class = PostForm
    success_url = reverse_lazy('post_list')


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

    def form_valid(self, form):
        new = form.save(commit=False)
        if self.request.path == '/news/create/':
            new.post_tip_id = 1
        elif self.request.path == '/state/create/':
            new.post_tip_id = 2
            new.save()
        return super().form_valid(form)


class CategoryList(ListView):
    model = Category
    ordering = '-name'
    template_name = 'category.html'
    context_object_name = 'category'


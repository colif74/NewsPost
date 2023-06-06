from django.views.generic import ListView, DetailView, CreateView,\
    TemplateView, UpdateView, DeleteView
from .models import Post, Author, BaseRegisterForm
from .filters import PostFilter
from .forms import PostForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as AuthLoginView


class LoginView(AuthLoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
        return super().form_valid(form)


class MyView(PermissionRequiredMixin, CreateView):
    permission_required = ('news.Post')


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'endex.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='author').exists()
        return context


@login_required
def upgrade_me(request):
    user = request.user
    author_group = Group.objects.get(name='author')
    if not request.user.groups.filter(name='author').exists():
        author_group.user_set.add(user)
        return redirect('/')


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


# class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
#     template_name = 'article_edit.html'
#     permission_required = ('portal.update.post')
#     form_class = ProductForm
#     success_url = '/news/'
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



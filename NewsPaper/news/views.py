from django.views.generic import ListView
from .models import Post, Author, Category, Comment

class AuthorList(ListView):
    model = Author
    ordering = 'user'
    template_name = 'Author.html'
    context_object_name = 'Author'

class PostList(ListView):
    model = Post
    ordering = 'header'
    template_name = 'headerpost.html'
    context_object_name = 'Post'

class CommentList(ListView):
    model = Comment
    ordering = 'comment'
    template_name = 'comment.html'
    context_object_name = 'comment'

class CategoryList(ListView):
    model = Category
    ordering = 'post_or_news'
    template_name = 'category.html'
    context_object_name = 'category'


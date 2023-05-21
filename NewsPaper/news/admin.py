from django.contrib import admin
from .models import Author, Post, Category, PostCategory, Comment

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Category)

# Register your models here.

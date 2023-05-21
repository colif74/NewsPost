from django.urls import path
from .views import PostList, CategoryList, AuthorList, CommentList

urlpatterns = [path('', PostList.as_view()),
               path('', AuthorList.as_view()),
               path('', CommentList.as_view()),
               path('', CategoryList.as_view()),
               ]
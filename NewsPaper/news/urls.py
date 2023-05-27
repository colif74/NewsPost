from django.urls import path
from .views import PostList, CategoryList, AuthorList, PostDetail


urlpatterns = [path('', PostList.as_view(), name='posts'),
               path('author', AuthorList.as_view(), name='author'),
               path('category', CategoryList.as_view(), name='category'),
               #path('<int: pk>', PostDetail.as_view()),
               ]

from django.urls import path
from .views import PostList, CategoryList, AuthorList, PostDetail, create_post


urlpatterns = [path('', PostList.as_view(), name='posts'),
               path('author/', AuthorList.as_view(), name='author'),
               path('category/', CategoryList.as_view(), name='category'),
               path('<int:pk>', PostDetail.as_view()),
               path('create/', create_post, name='create_post'),
               ]

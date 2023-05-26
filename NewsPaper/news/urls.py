from django.urls import path
from .views import PostList, CategoryList, AuthorList, AuthorDetail, CommentList

urlpatterns = [path('', PostList.as_view()),
               path('Author', AuthorList.as_view()),
               path('', CategoryList.as_view()),
               #path('<int:pk>', AuthorDetail.as_view()),
               ]
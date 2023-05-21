from django.urls import path
from .views import PostList, CategoryList

urlpatterns = [path('', PostList.as_view()),]
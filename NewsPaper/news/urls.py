from django.urls import path
from .views import PostList, CategoryList, AuthorList, PostDetail, PostCreate, PostUpdate, PostDelete


urlpatterns = [path('', PostList.as_view(), name='posts-list'),
               path('author/', AuthorList.as_view(), name='author'),
               path('category/', CategoryList.as_view(), name='category'),
               path('<int:pk>', PostDetail.as_view(), name='post_detail'),
               path('create/', PostCreate.as_view(), name='post_create'),
               path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
               path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
               ]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import PostList, CategoryList, AuthorList, PostDetail, PostCreate,\
    PostUpdate, PostDelete, StateDelete, StateUpdate, StateCreate, IndexView, BaseRegisterView

urlpatterns = [path('', IndexView.as_view()),
               path('login/', LoginView.as_view(template_name = 'news/login.html'), name='login'),
               path('logout/', LogoutView.as_view(template_name = 'news/logout.html'), name='logout'),
               path('signup/', BaseRegisterView.as_view(template_name = 'news/signup.html'), name='signup'),
               path('news/', PostList.as_view(), name='posts-list'),
               path('author/', AuthorList.as_view(), name='author'),
               path('category/', CategoryList.as_view(), name='category'),
               path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
               path('news/create/', PostCreate.as_view(), name='post_create'),
               path('news/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
               path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
               path('state/<int:pk>/update/', StateUpdate.as_view(), name='state_update'),
               path('state/<int:pk>/delete/', StateDelete.as_view(), name='state_delete'),
               path('state/create/', StateCreate.as_view(), name='state_create'),
               ]

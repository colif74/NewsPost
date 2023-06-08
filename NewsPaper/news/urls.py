from django.urls import path
from .forms import upgrade_me
from django.contrib.auth.views import LoginView, LogoutView
from .views import PostList, AuthorList, PostDetail, PostCreate,\
    PostUpdate, PostDelete, StateDelete, StateUpdate, StateCreate, IndexView, BaseRegisterView, CategoryList

urlpatterns = [path('', IndexView.as_view()),
               path('upgrade/', upgrade_me, name='upgrade'),
               path('login/', LoginView.as_view(template_name='login.html'), name='login'),
               path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
               path('signup/', BaseRegisterView.as_view(template_name='news/signup.html'), name='signup'),
               path('news/', PostList.as_view(), name='posts-list'),
               path('author/', AuthorList.as_view(), name='author'),
               path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
               path('news/create/', PostCreate.as_view(), name='post_create'),
               path('news/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
               path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
               path('state/<int:pk>/update/', StateUpdate.as_view(), name='state_update'),
               path('state/<int:pk>/delete/', StateDelete.as_view(), name='state_delete'),
               path('state/create/', StateCreate.as_view(), name='state_create'),
               path('category/<int:pk>', CategoryList.as_view(), name='category_list'),
               path('category/', CategoryList.as_view(), name='category_list'),
               ]

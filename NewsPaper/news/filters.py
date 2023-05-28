from django_filters import FilterSet
from .models import Post

# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
   class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'heander': ['icontains'],
           # количество товаров должно быть больше или равно
           'quantity': ['gt'],
           'post_tip': [post_tip__in =
               'news',  # цена должна быть меньше или равна указанной
               'states',  # цена должна быть больше или равна указанной
           ],
       }
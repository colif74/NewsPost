from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models import Sum
from django.contrib.contenttypes.fields import GenericRelation
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    rating = models.IntegerField(default=0)

    def update_rating(self):
        pass

economy = 'EC'
politician = 'PL'
worldnews = 'WN'
hostnews = 'HN'
sport = 'SP'

POSITION = [
        (economy, 'Экономика'),
        (politician, 'Политика'),
        (worldnews, 'Мировые новости'),
        (hostnews, 'Местные новости'),
        (sport, 'Спортивные новости')
          ]

class Category(models.Model):
       category = models.CharField(max_length=2, choices=POSITION, default='HN')

class Post(models.Model):
    date_in = models.DateField(auto_now_add=True)
    header = models.CharField(max_length=255)
    contents = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def preview(self):
          return f"{self.contents[:124]}..."



class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)



class Comment(models.Model):
    text_comment = models.TextField()
    date_creat = models.DateField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Post, on_delete=models.CASCADE)



class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    LIST = (
        (LIKE, 'нравится'),
        (DISLIKE, 'не нравится')
    )

    znak = models.SmallIntegerField(verbose_name=('голос'), choices=LIST)
    users = models.ForeignKey(User, verbose_name=('Пользователь'), on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    #object = LikeDislikeManager()

class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        return self.get_queryset().filter(znak__gt=0)

    def dislike(self):
        return self.get_queryset().filter(znak__lt=0)

    def sum_rating(self):
        return self.get_queryset().aggregate(Sum('znak')).get('znak__sum') or 0

    def articles(self):
        return self.get_queryset().filter(content_type__model='article').order_by('-articles__pub_date')

    def comments(self):
        return self.get_queryset().filter(content_type__model='comment').order_by('-comments__pub_date')

class Article(models.Model):
        votes = GenericRelation(LikeDislike, related_query_name='articles')

class Coment(models.Model):
    votes = GenericRelation(LikeDislike, related_query_name='comments')



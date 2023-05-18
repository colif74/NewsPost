from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from django.db.models import Sum
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.fields import GenericRelation


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    rating = models.IntegerField(default=0)

    def update_rating(self):
        author_rating_post = Post.objects.filter(author_id=self.pk).aggregate(post_rating_sum=Coalesce(Sum('rating_post') * 3, 0))
        author_rating_comment = Comment.objects.filter(user_id=self.user).aggregate(comment_rating_sum=Coalesce(Sum('rating_comment'), 0))
        author_rating_comment_post = Comment.objects.filter(post__author__id=self.user).aggregate(post_comment_rating_sum=Coalesce(Sum('rating_comment'), 0))
        self.rating = author_rating_post['post_rating_sum'] + author_rating_comment['comment_rating_sum'] + author_rating_comment_post['post_comment_rating_sum']
        self.save()

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
       post_or_news = models.CharField(max_length=4, help_text="news" or "post")
       category = models.CharField(max_length=2, choices=POSITION, default='HN')

class Post(models.Model):
    objects = None
    date_in = models.DateField(auto_now_add=True)
    header = models.CharField(max_length=255)
    contents = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')
    rating_post = models.IntegerField(default=0)

    def likes(self):
        self.rating_post += 1
        self.save()

    def dislikes(self):
        self.rating_post -= 1
        self.save()


    def preview(self):
        return f"{self.contents[:124]}..."



class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    objects = None
    text_comment = models.TextField()
    date_creat = models.DateField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
         self.rating_comment -= 1
         self.save()


# class LikeDislike(models.Model):
#     LIKE = 1
#     DISLIKE = -1
#
#     LIST = (
#         (LIKE, 'нравится'),
#         (DISLIKE, 'не нравится')
#     )
#
#     znak = models.SmallIntegerField(verbose_name=('голос'), choices=LIST)
#     users = models.ForeignKey(User, verbose_name=('Пользователь'), on_delete=models.CASCADE)
#
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey()
#
#
# class LikeDislikeManager(models.Manager):
#     use_for_related_fields = True
#
#     def likes(self):
#         return self.get_queryset().filter(znak__gt=0)
#
#     def dislike(self):
#         return self.get_queryset().filter(znak__lt=0)
#
#     def sum_rating(self):
#         return self.get_queryset().aggregate(Sum('znak')).get('znak__sum') or 0
#
#     def articles(self):
#         return self.get_queryset().filter(content_type__model='article').order_by('-articles__pub_date')
#
#     def comments(self):
#         return self.get_queryset().filter(content_type__model='comment').order_by('-comments__pub_date')
#
# class Article(models.Model):
#         votes = GenericRelation(LikeDislike, related_query_name='articles')
#
# class Coment(models.Model):
#     votes = GenericRelation(LikeDislike, related_query_name='comments')
#


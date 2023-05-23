from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from django.db.models import Sum
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.fields import GenericRelation


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        author_rating_post = Post.objects.filter(author_id=self.pk).\
            aggregate(post_rating_sum=Coalesce(Sum('rating_post') * 3, 0))
        author_rating_comment = Comment.objects.filter(user_id=self.user).\
            aggregate(comment_rating_sum=Coalesce(Sum('rating_comment'), 0))
        author_rating_comment_post = Comment.objects.filter(post__author__id=self.user).\
            aggregate(post_comment_rating_sum=Coalesce(Sum('rating_comment'), 0))
        self.rating = author_rating_post['post_rating_sum'] + author_rating_comment['comment_rating_sum'] \
            + author_rating_comment_post['post_comment_rating_sum']
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)


class Post(models.Model):
    objects = None
     news = 'NW'
    states = 'PS'

    TYPE = [
        (news, 'Новость'),
        (states, 'Статья')
    ]

    post_tip = models.CharField(max_length=10, choices=TYPE, default=states)
    date_in = models.DateField(auto_now_add=True)
    header = models.CharField(max_length=255)
    contents = models.TextField(blank=True)
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
    text_comment = models.TextField(blank=True)
    date_in = models.DateField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()

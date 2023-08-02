from .models import *
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Author
       fields = ['id', 'user', ]


class PostSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Post
       fields = ['post_tip', 'header', 'content', 'author', ]


# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Category
#        fields = ['id', 'name', ]

from django.db import models
from django.contrib.auth.models import User
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

@register(AlgoliaIndex)
class Content(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
@register(Content)
class ContentIndex(AlgoliaIndex):
    fields = ('title', 'body', 'author', 'created_at')
    settings = {'searchableAttributes': ['title', 'body']}
    index_name = 'content'
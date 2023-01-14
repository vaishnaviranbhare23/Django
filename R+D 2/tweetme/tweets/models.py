from django.db import models
import random
from django.conf import settings
from django.db.models.deletion import CASCADE

User = settings.AUTH_USER_MODEL

# Create your models here.

# Blank= True -> Not required in Django
# Null = True -> Not required in Database


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Tweet(models.Model):
    # id = models.AutoField(primary_key=True)
    # models.CASCADE if the owner user is deleted then the tweets(object) are deleted too
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200, blank=True, null=True)
    images = models.FileField(upload_to='images/', blank=True, null=True)
    likes = models.ManyToManyField(
        User, related_name='tweet_user', blank=True, through=TweetLike)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    @property
    def is_retweet(self):
        return self.parent != None

    # def __str__(self) -> str:
    #     return self.content

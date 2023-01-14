from django.contrib import admin
from django.contrib.admin.sites import site
from django.db import models
from .models import Tweet, TweetLike
# Register your models here.

# To add search box in admin


class TweetLikeAdmin(admin.TabularInline):
    model = TweetLike


class TweetAdmin(admin.ModelAdmin):
    inlines = [TweetLikeAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']

    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetAdmin)

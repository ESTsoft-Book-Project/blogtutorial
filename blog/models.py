from django.db import models
from django.contrib.auth.models import User
import tinymce.models


class Article(models.Model):
    title = models.CharField(max_length=255)
    # rich text editor HTML Field below
    content = tinymce.models.HTMLField()
    # automatically fill the date field with today
    date = models.DateField(auto_now_add=True)
    # models.CASCADE will delete all user's articles on delete account
    # DO_NOTHING, SET_NULL 등의 옵션이 있으니 참고바람.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # as default, all articles are being not be featured
    featured = models.BooleanField(default=False)
    # user can hit like button
    likes = models.ManyToManyField(User, related_name="likes", blank=True)

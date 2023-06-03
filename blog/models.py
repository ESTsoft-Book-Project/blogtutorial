from django.db import models
import users.models
import tinymce.models


class Article(models.Model):
    title = models.CharField(max_length=255)

    # rich text editor HTML Field below
    content = tinymce.models.HTMLField()

    # automatically fill the date field with today
    date = models.DateField(auto_now_add=True)

    # models.CASCADE will delete all user's articles on delete account
    # DO_NOTHING, SET_NULL 등의 옵션이 있으니 참고바람.
    author = models.ForeignKey(users.models.User, on_delete=models.CASCADE, related_name="author")

    # as default, all articles are being not be featured
    featured = models.BooleanField(default=False)

    # user can hit like button
    likes = models.ManyToManyField(users.models.User, related_name="likes", blank=True)

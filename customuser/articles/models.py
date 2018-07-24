# articles/models.py

# Create your models here.

from django.db import models
from django.conf import settings
from django.urls import reverse


class Article(models.Model):
    # Here's where we'll describe the fields of the article
    title = models.CharField(max_length=300)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


# Another way to add comment functionality would have been to create a dedicated "Comments" app, but this is kind of
# overkill.


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')
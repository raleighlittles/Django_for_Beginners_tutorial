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
# blog/models.py
from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    # CASCADE: when the referenced object is deleted, also delete the objects that have references to it
    # Use ForeignKey here because we want a 'many-to-one' relationship, i.e. one user can write multiple posts
    # auth.User is the built-in Django model for users
    # Since we're using a ForeignKey, we must specify an on_delete setting
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    # As usual, it is good practice to always overload the str() operator for the model?
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

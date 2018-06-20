# posts/models.py
from django.db import models

# Create your models here.

class Post(models.Model):
     # create a database model called 'Post' (note that models are singular names)
     # which stores content of the type 'TextField'. The full list of models is here: 
     # https://docs.djangoproject.com/en/2.0/ref/models/fields/
    text = models.TextField() 

    def __str__(self):
        # override the str() operator for the Post object to print the first 50 
        # characters of the message. Its a good idea to override your string operator
        # for all of your models
        return self.text[:50]

# post/views.py
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.

class HomePageView(ListView): # ListView is used on a page representing a list of objects
    model = Post # must explictly declare which model to use
    template_name = 'home.html'
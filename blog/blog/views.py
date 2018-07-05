# blog/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    # explicitly list the fields you want to use, we're assume that the author of the post is not changing..
    # if it was, use '__all__'
    fields=['title', 'body']
    template_name = 'post_edit.html'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    # use reverse_lazy when you dont necessarily want to execute the url,this makes it so that the url redirect
    # wont happen until the view has finished deleting the blog post.
    success_url = reverse_lazy('home')

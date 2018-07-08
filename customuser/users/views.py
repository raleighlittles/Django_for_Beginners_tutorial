# users/views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

# Create your views here.

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    # where to send the user after they've been successfully logged in
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


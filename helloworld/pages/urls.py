#pages/urls.py
from django.urls import path

from . import views # the period here references current directory

urlpatterns = [
    path('', views.homePageView, name='home')
]
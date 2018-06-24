# blog/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('',views.BlogListView.as_view(), name='home'),
    # the "pk" below refers to the 'primary key' that django automatically creates for database models
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
]
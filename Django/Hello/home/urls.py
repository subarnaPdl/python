from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blog', views.blog, name='blog'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]

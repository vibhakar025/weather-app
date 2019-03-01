from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    url(r'delete/(?P<cityn>[0-9]+)/', views.delete, name='delete'),

]
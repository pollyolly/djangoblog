from django.shortcuts import render
from django.urls import include, path
from django.http import HttpResponse
#import blogpost.views as views2 #import views from blogpost
from . import views

urlpatterns = [
    path('', views.home,name="homepage"),
    #path('blogpost/<str:pk>/', views2.post, name="postname"),
    #path('admin/blogpost/post/<str:pk>/change/',views.editpost,name="editpost")
]

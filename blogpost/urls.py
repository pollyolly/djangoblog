from django.shortcuts import render
from django.urls import include, path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('blogpost/<int:pk>/', views.post,name="postname"),
    path('addcomment/',views.addcomment,name="addcomment"),
    path('admin/blogpost/post/<int:pk>/change/',views.editpost,name="editpost")
]

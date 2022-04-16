from django.shortcuts import render
from django.urls import include, path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('',views.setting)
]

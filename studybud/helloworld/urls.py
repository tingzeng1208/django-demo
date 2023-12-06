from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("hello", views.hello),
    path("hello_html", views.hello_html),
    path("hello_var", views.hello_var)
]


from django.urls import path
from . import views
# from .views import home, hubzone

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('hubzone/', views.hubzone, name='hubzone'),
]


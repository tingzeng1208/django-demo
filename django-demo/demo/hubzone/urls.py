
from django.urls import path
from . import views
# from .views import home, hubzone

urlpatterns = [

    path('', views.home),
    path('home/', views.home),
    path('hubzone/', views.hubzone, name='hubzone'),    
    path('api/employee/', views.EmployeeView.as_view(), name="api/employee"),
    path('api/firm/', views.FirmView.as_view(), name="api/firm"),
]


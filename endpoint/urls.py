from django.urls import path, include
from . import views

urlpatterns = [
    path('search', views.api_req, name='api_req'),
    path('search/', views.api_req, name='api_req'),
]

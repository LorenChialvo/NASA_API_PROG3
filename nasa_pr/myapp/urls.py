from django.urls import path
from . import views

urlpatterns = [
    path('', views.apod_view, name='apod_view'),
    path('apod/', views.apod_view, name='apod'),
]

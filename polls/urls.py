from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('map/', views.map, name='map'),
    path('weather', views.weather, name='weather'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
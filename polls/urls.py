from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('map/', views.map, name='map'),
    path('weather', views.weather, name='weather'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html')),
]
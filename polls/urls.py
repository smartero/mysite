from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as polls_views

urlpatterns = [
    path('', polls_views.index, name='index'),
    path('offer/', polls_views.offer, name='offer'),
    path('register/', polls_views.register, name='register'),
    path('login/', polls_views.login, name='login'),
    path('logout/', auth_views.LogoutView. as_view(template_name='polls/logout.html'), name='logout'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html')),
]
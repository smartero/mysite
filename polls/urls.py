from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as polls_views

urlpatterns = [
    path('', polls_views.index, name='index'),
    path('offer/', polls_views.offer, name='offer'),
    path('<int:offer_id>', polls_views.offer_details, name='offer_details'),
    path('register/', polls_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='polls/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='polls/logout.html'), name='logout'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html')),
]
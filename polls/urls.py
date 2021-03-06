from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from polls import views as polls_views
from polls.views import SearchListView

urlpatterns = [
    path('', polls_views.index, name='index'),
    path('make_offer/', polls_views.make_offer, name='make_offer'),
    path('register/', polls_views.register, name='register'),
    path('profile/', polls_views.profile, name='profile'),
    path('profile/<int:pk>/', polls_views.profile, name='profile'),
    path('search/', SearchListView.as_view(), name='search'),
    path('details/<int:pk>/', polls_views.details, name='details'),
    path('login/', auth_views.LoginView.as_view(template_name='polls/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='polls/logout.html'), name='logout'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html')),
    path('edit_profile/', polls_views.edit_profile, name='edit_profile'),
]
# only in DEBUG mode, url pattern for images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
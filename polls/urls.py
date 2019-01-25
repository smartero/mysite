from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import ResultListView

from polls import views as polls_views

urlpatterns = [
    path('', ResultListView.as_view(), name='index'),
    path('offer/', polls_views.offer, name='offer'),
    path('result/', ResultListView.as_view(), name='result'),
    path('register/', polls_views.register, name='register'),
    path('profile/', polls_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='polls/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='polls/logout.html'), name='logout'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html')),
]

# only in DEBUG mode, url pattern for images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from .views import user_login, user_logout, register, profile
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = ([
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
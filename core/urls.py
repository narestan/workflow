# core/urls.py

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__reload__/', include('django_browser_reload.urls', namespace='django_browser_reload')),
    path('', include(('users.urls', 'users'), namespace='users')),
    path('materials/', include(('materials.urls','materials'), namespace='materials')),
    path('reqmat/', include(('reqmat.urls','reqmat'), namespace='reqmat')),
]

AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'

from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Ensure this line is correct
]
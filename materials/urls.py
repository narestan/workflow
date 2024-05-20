from django.urls import path
from . import views


app_name = 'materials'


urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/new/', views.category_create, name='category_create'),
    path('category/<int:category_id>/items/', views.item_list, name='item_list'),
    path('category/<int:category_id>/items/new/', views.item_create, name='item_create'),
]

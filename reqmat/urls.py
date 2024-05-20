# reqmat/urls.py

from django.urls import path
from reqmat.views import create_profit_request, create_glass_request, create_other_request, RequestListView

app_name = "reqmat"

urlpatterns = [
    path('', RequestListView.as_view(), name='request_list'),
    path('profit/', create_profit_request, name='create_profit_request'),
    path('glass/', create_glass_request, name='create_glass_request'),
    path('other/', create_other_request, name='create_other_request'),
]
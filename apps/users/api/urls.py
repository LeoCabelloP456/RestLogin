from django.urls import path
from apps.users.api.api import user_api_view, user_detail_api_view
from apps.users.api.views import registro_view

app_name= "users"

urlpatterns = [
    path('usuario/', user_api_view, name='usuario_api'),
    path('usuario/<int:pk>/', user_detail_api_view, name='usuario_detail_api_view'),
    path('registro', registro_view, name="registro"),
]
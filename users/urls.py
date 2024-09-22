from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.user_list, name='user_list'),
    path('product/<int:user_id>/', views.user_detail, name='user_detail'),
]

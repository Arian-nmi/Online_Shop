from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('products/', views.products, name='product_list'),
=======
    path('products/', views.product_list_creation, name='product_list'),
    path('products/', views.product_list, name='product_list'),
>>>>>>> 8da2cb7b478197b9389d7f1535fcc5b4cb1cb9f2
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/<int:category_id>/products/', views.category_product_list, name='category_product_list'),
]

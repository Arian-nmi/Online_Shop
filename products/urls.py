from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('products/', views.product_list_creation, name='product_list'),
=======
    path('products/', views.product_list, name='product_list'),
>>>>>>> 9750d19510afba2425c8776ebd6db6b453cef295
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/<int:category_id>/products/', views.category_product_list, name='category_product_list'),
]

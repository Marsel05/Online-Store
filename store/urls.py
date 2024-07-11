from django.contrib.auth.urls import path
from .views import *

urlpatterns = [
    path('user/', CustomUserViewSets.as_view({"get": "list", 'post': 'create'}), name='user_list'),
    path('user/<int:pk>/', CustomUserViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': 'destroy'}), name='user_detail'),

    path('category/', CategoryViewSets.as_view({"get": "list", 'post': 'create'}), name='category_list'),
    path('category/<int:pk>/', CategoryViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': 'destroy'})),

    path('product/', ProductViewSets.as_view({"get": "list", 'post': 'create'}), name='product_list'),
    path('product/<int:pk>/', ProductViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': 'destroy'}), name='product_list'),

    path('order/', OrderViewSets.as_view({"get": "list", 'post': 'create'}), name='order_list'),
    path('order/<int:pk>/', OrderViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': 'destroy'}), name='order_detail'),

    path('order_item/', OrderItemViewSets.as_view({"get": "list", 'post': 'create'}), name='order_item_list'),
    path('order_item/<int:pk>/', OrderItemViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': 'destroy'}), name='order_item_detail'),

    path('payment/', PaymentViewSets.as_view({"get": "list", 'post': 'create'}), name='payment_list'),
    path('payment/<int:pk>/', PaymentViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': 'destroy'}), name='payment_detail'),

]
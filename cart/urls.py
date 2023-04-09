from django.urls import path
from cart import views



app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:laptop_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:laptop_id>/', views.cart_remove, name='cart_remove'),
]
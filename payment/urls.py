from django.urls import path
from .import views
urlpatterns = [
    path("checkout",views.checkout,name="checkout"),
    path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('order-history/', views.order_history, name='order_history'),
    path('shipped_dash', views.shipped_dash, name="shipped_dash"),
    path('unshipped_dash', views.unshipped_dash, name="unshipped_dash"),
]

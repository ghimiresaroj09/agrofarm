from django.urls import path
from .import views
urlpatterns = [
    path("",views.home,name="home"),
    path("product/<int:pk>",views.product, name="product"),
    path("add_product",views.add_product, name="add_product"),
    path('category/<str:cname>',views.category, name='category'),
    path("search/", views.search, name="search"),
    path("sale/", views.sale, name="sale"),
]

from django.urls import path, include
from .views import list_products, find_products

urlpatterns = [
    path('', list_products, name="list_products"),
    path('find_products/<slug:nome>', find_products, name="find_products"),
]

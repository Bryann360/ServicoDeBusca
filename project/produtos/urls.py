from django.urls import path, include
from .views import list_products

urlpatterns = [
    path('', list_products, name="list_products"),
]

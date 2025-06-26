from django.urls import path
from .views import category_list, category_create, product_list, product_create

urlpatterns = [
    path("categories/", category_list),
    path("categories/create/", category_create),
    path("", product_list),
    path("create/", product_create),
]

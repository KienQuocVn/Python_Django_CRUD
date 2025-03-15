from django.urls import path
from .views import product_create,product_list,product_update,product_delete, product_sell

urlpatterns = [
    path('create/', product_create, name="product_create"),
    path('', product_list, name="product_list"),
    path('update/<int:product_id>/', product_update, name="product_update"),
    path('delete/<int:product_id>/', product_delete, name="product_delete"),
    path('sell/<int:product_id>/', product_sell, name="product_sell")
]

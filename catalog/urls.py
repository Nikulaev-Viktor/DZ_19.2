from django.urls import path
from catalog.views import contacts, product_list, product_detail, base
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    path('', base, name='base'),
    path('product_list/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('contacts/', contacts, name='contacts')
]

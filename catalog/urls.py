from django.urls import path
from catalog.views import contacts, product_list, product_detail
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    # path('', base, name='base'),
    path('', product_list, name='product_list'),
    # path('product_list/', product_list, name='product_list'),
    path('product_detail/<int:pk>', product_detail, name='product_detail'),
    path('contacts/', contacts, name='contacts')
]

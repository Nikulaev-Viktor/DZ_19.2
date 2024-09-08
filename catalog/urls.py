from django.urls import path
from catalog.views import ProductListView, ProductDetailView, contacts
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    # path('', base, name='base'),
    path('', ProductListView.as_view(), name='product_list'),
    # path('product_list/', product_list, name='product_list'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', contacts, name='contacts')
    # path('contacts/', ContactsTemplateView. as_view(), name='contacts')
]

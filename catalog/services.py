from catalog.models import Product
from config.settings import CASHES_ENABLED
from django.core.cache import cache


def get_product_from_cache():
    """Получает данные по продуктам из кэша, если кеш пуст, то данные получает из БД"""
    if not CASHES_ENABLED:
        return Product.objects.all()
    key = "product_list"
    product = cache.get(key)
    if product is not None:
        return product
    product = Product.objects.all()
    cache.set(key, product)
    return product

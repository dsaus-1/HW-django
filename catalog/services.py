from django.conf import settings
from django.core.cache import cache

from catalog.models import Product, Category


def cache_products(product_item):
    queryset = Product.objects.filter(product_name=product_item)
    if settings.CACHE_ENABLED:
        key = f'product_{product_item}'
        cache_data = cache.get(key)

        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)

        return cache_data

def cache_categories():
    queryset = Category.objects.all()
    if settings.CACHE_ENABLED:
        key = f'all_category'
        cache_data = cache.get(key)

        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)

        return cache_data

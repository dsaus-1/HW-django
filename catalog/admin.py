from django.contrib import admin

from catalog.models import Category, Product, Blog

# admin.site.register(Category)
# admin.site.register(Product)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category',)
    search_fields = ('product_name', 'descriptions',)
    list_filter = ('category',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('header', 'slug', 'content', 'publication_status', 'number_of_views', )
    search_fields = ('slug', 'header', 'publication_status',)
    list_filter = ('publication_status',)
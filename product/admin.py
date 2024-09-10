from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','image_tag','price', 'category', 'is_sale','sale_price','out_of_stock')
    search_fields = ('name', 'description')
    list_per_page=10
    list_filter=('category','is_sale','out_of_stock')
    list_editable=('is_sale','sale_price','out_of_stock')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
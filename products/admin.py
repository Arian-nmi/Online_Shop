from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('name',)
=======
    list_display = 'name'
>>>>>>> 8da2cb7b478197b9389d7f1535fcc5b4cb1cb9f2


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity', 'category')
    list_filter = ('category',)
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
<<<<<<< HEAD
admin.site.register(Product, ProductAdmin)
=======
admin.site.register(Product,  ProductAdmin)
>>>>>>> 8da2cb7b478197b9389d7f1535fcc5b4cb1cb9f2

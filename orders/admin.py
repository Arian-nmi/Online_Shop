from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_created', 'status')
    search_fields = ('user__username',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')
    search_fields = ('product__name', 'order__id')


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)

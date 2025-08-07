from django.contrib import admin
from .models import MenuItem, Order
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display=('name','price','is_available')
    search_fields=('name',)
    list_filter=('is_available',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','customer','status', 'total_amount')
    list_filter=('status',)
    search_fields=('customer_username',)
    filter_horizantal=('items',)
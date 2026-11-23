from django.contrib import admin

from rms.models import *

# Register your models here.
admin.site.register(Category)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name', 'category__name')
    list_filter = ('category__name',)
admin.site.register(Menu, MenuAdmin)

class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_available', 'reservation')
    list_filter =('is_available',)
admin.site.register(Table, TableAdmin)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'minimum_stock')
    search_fields = ('name',)
admin.site.register(Inventory, InventoryAdmin)

class OrderItemInline(admin.TabularInline):
    model = Order_Item
    extra = 0
    autocomplete_fields =('menu',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'table', 'status', 'payment_status', 'total_price',)
    list_filter = ('status', 'payment_status')
    search_fields = ('table__name', 'user__username')
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(Order_Item)

admin.site.register(Review)
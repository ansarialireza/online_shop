# admin.py

from django.contrib import admin
from .models import Order, OrderItem, Customcurtain, Cornice, Floorcoverings, NormalProducts

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at', 'get_total_items']  # Include 'get_total_items'
    inlines = [OrderItemInline]
    search_fields = ['user__name']  # Add search field for user's name

    def get_total_items(self, obj):
        return obj.items.count()

    get_total_items.short_description = 'Total Items'  # Column header

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'texture_code', 'get_user', 'get_order_total']  # Include 'get_user' and 'get_order_total'
    search_fields = ['order__user__name', 'product__title']  # Adjust these based on your models
    list_filter = ['order__user__name', 'order__created_at']  # Adjust these based on your models

    def get_user(self, obj):
        return obj.order.user

    get_user.short_description = 'User'  # Column header for user

    def get_order_total(self, obj):
        return obj.order.items.count()

    get_order_total.short_description = 'Order Total'  # Column header for order total

class CustomcurtainAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'texture_code', 'quantity', 'length', 'width', 'needs_curtain_rod']
    search_fields = ['order__user__name', 'product__title']
    list_filter = ['order__user__name', 'needs_curtain_rod']

    class Meta:
        verbose_name = 'پرده سفارشی'
        verbose_name_plural = 'پرده‌های سفارشی'

class CorniceAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'texture_code', 'cornice_7', 'cornice_9', 'Gordeh', 'Miane', 'Tasho', 'Scouti']
    search_fields = ['order__user__name', 'product__title']
    list_filter = ['order__user__name']

    class Meta:
        verbose_name = 'قرنیز'
        verbose_name_plural = 'قرنیزها'

class FloorcoveringsAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'texture_code', 'quantity', 'glue_4kg', 'glue_10kg']
    search_fields = ['order__user__name', 'product__title']
    list_filter = ['order__user__name']

    class Meta:
        verbose_name = 'پوشش کف'
        verbose_name_plural = 'پوشش‌های کف'

class NormalProductsAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'texture_code', 'quantity']
    search_fields = ['order__user__name', 'product__title']
    list_filter = ['order__user__name']

    class Meta:
        verbose_name = 'محصول عادی'
        verbose_name_plural =  'محصولات عادی'

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Customcurtain, CustomcurtainAdmin)
admin.site.register(Cornice, CorniceAdmin)
admin.site.register(Floorcoverings, FloorcoveringsAdmin)
admin.site.register(NormalProducts, NormalProductsAdmin)

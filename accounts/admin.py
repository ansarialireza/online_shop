# accounts/admin.py
from django.contrib import admin
from jalali_date import date2jalali
from django.utils.html import format_html
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'phone_number', 'is_active', 'is_hurry', 'customer_type', 'postal_code', 'province', 'city', 'last_login', 'date_created_jalali')

    list_display_links = ('name', 'lastname', 'phone_number')
    list_editable = ('is_active', 'customer_type',)
    exclude = ('groups', 'user_permissions', 'is_superuser', 'password',)
    search_fields = ('name', 'lastname', 'phone_number')
    list_filter = ('is_active', 'customer_type', 'date_of_registration')
    filter_horizontal = ('groups', 'user_permissions')

    def date_created_jalali(self, obj):
        jalali_date = date2jalali(obj.date_of_registration)
        return jalali_date.strftime('%Y/%m/%d')

    date_created_jalali.short_description = 'تاریخ ثبت نام'
    date_created_jalali.admin_order_field = 'date_of_registration'


admin.site.register(User, UserAdmin)

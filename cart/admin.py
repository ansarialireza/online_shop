# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
# from accounts.models import User as CustomUser

# from .models import Cart, CartItem

# class CartItemInline(admin.TabularInline):
#     model = CartItem
#     extra = 1

# class CartAdmin(admin.ModelAdmin):
#     list_display = ['user', 'created_at']
#     inlines = [CartItemInline]

# admin.site.register(Cart, CartAdmin)

# class CustomUserAdmin(CustomUser):
#     inlines = [CartItemInline]

# # Register the default User model with the custom admin class
# # admin.site.register(User, CustomUserAdmin)

# # Register the custom User model
# # admin.site.register(CustomUser)

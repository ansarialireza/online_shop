# # models.py
# from django.conf import settings
# from django.db import models
# from products.models import *
# from django.db.models.signals import post_save
# from django.dispatch import receiver
 
# class Cart(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart', verbose_name='کاربر')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

#     class Meta:
#         verbose_name = 'سبد خرید'
#         verbose_name_plural = 'سبدهای خرید'

#     def __str__(self):
#         # user_info = f"{self.user.phone_number}" if self.user and hasattr(self.user, 'phone_number') else "Anonymous User"
#         # return f"Cart for {user_info}"
#         return "cart"
# @receiver(post_save, sender=Cart)
# def create_cart(sender, instance, created, **kwargs):
#     """
#     Signal receiver for creating a CartItem instance when a Cart is created.
#     """
#     if created:
#         print(f"Cart created for user: {instance.user}")
#         CartItem.objects.create(cart=instance)
#         print(f"CartItem created for Cart: {instance}")

# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name='سبد خرید')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
#     quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')
#     texture = models.ForeignKey(Texture, on_delete=models.CASCADE, null=True, blank=True, related_name='cart_items', verbose_name='تکسچر ')
#     # custom_curtain_info = models.OneToOneField(Customcurtain, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='اطلاعات پرده سفارشی')

#     class Meta:
#         verbose_name = 'آیتم سبد خرید'
#         verbose_name_plural = 'آیتم‌های سبد خرید'

#     def __str__(self):
#         return f"{self.quantity} x {self.product.title} ({self.selected_texture.code}) in {self.cart.user.phone_number}'s cart"

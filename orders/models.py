# models.py

from django.db import models
from products.models import Product
from accounts.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")

    def __str__(self):
        return f'سفارش دهنده - {self.user}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    texture_code = models.IntegerField(verbose_name="کد تکسچر")

    def __str__(self):
        return f'{self.product}'

class Customcurtain(OrderItem):
    length = models.FloatField(null=True, blank=True, verbose_name="طول")
    quantity = models.PositiveIntegerField(default=1, verbose_name="تعداد")
    width = models.FloatField(null=True, blank=True, verbose_name="عرض")
    needs_curtain_rod = models.BooleanField(default=False, null=True, blank=True, verbose_name="نیاز به چوب پرده")

    class Meta:
        verbose_name = 'پرده سفارشی'
        verbose_name_plural = 'پرده‌های سفارشی'

    def __str__(self):
        return f'Custom Curtain - {self.product} - Quantity: {self.quantity}'

class Cornice(OrderItem):
    cornice_7 = models.PositiveIntegerField(null=True, blank=True, verbose_name='قرنیز 7 سانتی')
    cornice_9 = models.PositiveIntegerField(null=True, blank=True, verbose_name='قرنیز 9 سانتی')
    Gordeh = models.PositiveIntegerField(null=True, blank=True, verbose_name="گرده")
    Miane = models.PositiveIntegerField(null=True, blank=True, verbose_name="میانه")
    Tasho = models.PositiveIntegerField(null=True, blank=True, verbose_name="تاشو")
    Scouti = models.PositiveIntegerField(null=True, blank=True, verbose_name="اسکوتی")

    class Meta:
        verbose_name = 'قرنیز'
        verbose_name_plural = 'قرنیزها'

    def __str__(self):
        return f'Cornice - {self.product}'

class Floorcoverings(OrderItem):
    quantity = models.PositiveIntegerField(default=1, verbose_name="تعداد")
    glue_4kg = models.PositiveIntegerField(null=True, blank=True, verbose_name="چسب ۴ کیلوگرم")
    glue_10kg = models.PositiveIntegerField(null=True, blank=True, verbose_name="چسب ۱۰ کیلوگرم")

    class Meta:
        verbose_name = 'پوشش کف'
        verbose_name_plural = 'پوشش‌های کف'

    def __str__(self):
        return f'Floorcovering - {self.product} - Quantity: {self.quantity}'

class NormalProducts(OrderItem):
    quantity = models.PositiveIntegerField(default=1, verbose_name="تعداد")

    class Meta:
        verbose_name = 'محصول عادی'
        verbose_name_plural =  'محصولات عادی'

    def __str__(self):
        return f'Normal Product - {self.product} - Quantity: {self.quantity}'

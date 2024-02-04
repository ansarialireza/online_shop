from django.db import models

class IndexBanner(models.Model):
    CATEGORY_CHOICES = [
        ('sofa', 'مبلمان'),
        ('curtains', 'پرده'),
        ('decoration', 'دکوراسیون'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name='دسته‌بندی')
    large_image = models.ImageField(upload_to='banners/index/large/', verbose_name='تصویر بزرگ')
    small_image = models.ImageField(upload_to='banners/index/small/', verbose_name='تصویر کوچک')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'بنر'
        verbose_name_plural = 'بنرهای صفحه اصلی'

class SofaBanner(models.Model):
    small_sofa_image = models.ImageField(upload_to='banners/sofa/small/', verbose_name='تصویر کوچک مبل')
    small_sofafabric_image = models.ImageField(upload_to='banners/sofafabric/small/', verbose_name='تصویر کوچک پارچه مبلی')
    large_sofa_image_1= models.ImageField(upload_to='banners/sofa/large/', verbose_name=' 1 تصویر بزرگ')
    large_sofa_image_2= models.ImageField(upload_to='banners/sofa/large/', verbose_name=' 2 تصویر بزرگ')
    large_sofa_image_3= models.ImageField(upload_to='banners/sofa/large/', verbose_name=' 3 تصویر بزرگ')
    class Meta:
        verbose_name = 'بنر'
        verbose_name_plural = 'بنرهای صفحه مبل'
# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError(_('The Phone Number field must be set'))
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(phone_number=phone_number, password=password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    CUSTOMER_TYPE_CHOICES = [
        ('retail', 'مشتری خرد'),
        ('wholesale', 'مشتری عمده'),
        ('admin', 'ادمین سایت'),
    ]

    name = models.CharField(max_length=255, verbose_name=_("نام"))
    lastname = models.CharField(max_length=255, verbose_name=_("نام خانوادگی"))
    phone_number = models.CharField(max_length=15, unique=True, verbose_name=_("شماره تلفن"))
    postal_code = models.CharField(max_length=10, verbose_name=_("کد پستی"))
    province = models.CharField(max_length=255, verbose_name=_("استان"))
    city = models.CharField(max_length=255, verbose_name=_("شهر"))
    address = models.TextField(verbose_name=_("آدرس"))
    date_of_registration = models.DateTimeField(auto_now_add=True, verbose_name=_("تاریخ ثبت نام"))
    last_login = models.DateTimeField(auto_now_add=True, verbose_name=_("آخرین ورود"))
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    customer_type = models.CharField(max_length=10, choices=CUSTOMER_TYPE_CHOICES, default='retail', verbose_name='نوع کاربر')
    is_hurry = models.BooleanField(default=False, verbose_name=_("خرید همکار به صورت فوری"))
    objects = CustomUserManager()
    store_phone = models.CharField(max_length=15, null=True, blank=True, verbose_name=_("تلفن فروشگاه"))
    store_card = models.ImageField(null=True, blank=True, upload_to='financial_documents/', verbose_name=_("تصویر کارت فروشگاه"))
    photo_of_the_store = models.ImageField(null=True, blank=True, upload_to='financial_documents/', verbose_name=_("تصویر فروشگاه"))
    business_license = models.ImageField(null=True, blank=True, upload_to='financial_documents/', verbose_name=_("تصویر مجوز تجاری"))

    USERNAME_FIELD = 'phone_number'
    groups = models.ManyToManyField(Group, related_name='groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='permissions', blank=True)

    class Meta:
        verbose_name_plural = _("کاربران")

    def __str__(self):
        return f"{self.name} {self.lastname} - {self.city} - {self.phone_number} "
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

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(phone_number, password, **extra_fields)

# Uncomment the following line if you want to enforce required fields for superuser creation
# CustomUserManager.REQUIRED_FIELDS = ['name', 'lastname', 'postal_code', 'province', 'city', 'address']

class Image(models.Model):
    image = models.ImageField(upload_to='customer_images/', verbose_name='تصاویر')

    class Meta:
        verbose_name = _("تصویر")
        verbose_name_plural = _("تصاویر مدارک")

    def __str__(self):
        return f"تصویر {self.id}"

class User(AbstractBaseUser, PermissionsMixin):
    CUSTOMER_TYPE_CHOICES = [
        ('retail', 'خرد'),
        ('wholesale', 'عمده'),
    ]

    name = models.CharField(max_length=255, verbose_name=_("نام"))
    lastname = models.CharField(max_length=255, verbose_name=_("نام خانوادگی"))
    phone_number = models.CharField(max_length=15, unique=True, verbose_name=_("شماره تلفن"))
    postal_code = models.CharField(max_length=10, verbose_name=_("کد پستی"))
    province = models.CharField(max_length=255, verbose_name=_("استان"))
    city = models.CharField(max_length=255, verbose_name=_("شهر"))
    address = models.TextField(verbose_name=_("آدرس"))
    date_of_registration = models.DateTimeField(auto_now_add=True, verbose_name=_("تاریخ ثبت نام"))
    password = models.CharField(max_length=255, null=True, blank=True)
    last_login = models.DateTimeField(auto_now_add=True, verbose_name=_("آخرین ورود"))
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    customer_type = models.CharField(max_length=10, choices=CUSTOMER_TYPE_CHOICES, default='retail', verbose_name='نوع مشتری')

    USERNAME_FIELD = 'phone_number'
    # Uncomment the following line if you want to enforce required fields for superuser creation
    # REQUIRED_FIELDS = ['name', 'lastname', 'postal_code', 'province', 'city', 'address']

    groups = models.ManyToManyField(Group, related_name='groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='permissions', blank=True)

    class Meta:
        verbose_name_plural = _("کاربر")

    def __str__(self):
        return f"{self.name} {self.lastname}"

class PhoneNumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_phone_number', verbose_name=_("کاربر"))
    phone_number = models.CharField(_("شماره تلفن"), max_length=15, unique=True)
    verification_code = models.CharField(_("کد تایید"), max_length=6, blank=True, null=True)

    class Meta:
        verbose_name = _("شماره تلفن")
        verbose_name_plural = _("شماره‌های تلفن")

class Retailbuyer(User):
    class Meta:
        verbose_name_plural = _("خریداران خرده")
        verbose_name = _("خریدار خرده")

    def __str__(self):
        return f"خریدار خرده: {self.name} {self.lastname}"

class Majorbuyer(User):
    store_phone = models.CharField(max_length=15, null=True, blank=True, verbose_name=_("تلفن فروشگاه"))
    store_card = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='wholesale_customers_store_card', verbose_name=_("تصویر کارت فروشگاه"))
    photo_of_the_store = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True,
                                           related_name='wholesale_customers_photo_of_the_store',
                                           verbose_name=_("تصویر فروشگاه"))
    business_license = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True,
                                         related_name='wholesale_customers_business_license',
                                         verbose_name=_("تصویر مجوز تجاری"))

    class Meta:
        verbose_name_plural = _("خریداران عمده")
        verbose_name = _("خریدار عمده")

    def __str__(self):
        return f"خریدار عمده: {self.name} {self.lastname}"

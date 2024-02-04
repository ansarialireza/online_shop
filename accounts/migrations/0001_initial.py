# Generated by Django 4.2.5 on 2024-01-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('name', models.CharField(max_length=255, verbose_name='نام')),
                ('lastname', models.CharField(max_length=255, verbose_name='نام خانوادگی')),
                ('phone_number', models.CharField(max_length=15, unique=True, verbose_name='شماره تلفن')),
                ('postal_code', models.CharField(max_length=10, verbose_name='کد پستی')),
                ('province', models.CharField(max_length=255, verbose_name='استان')),
                ('city', models.CharField(max_length=255, verbose_name='شهر')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('date_of_registration', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت نام')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='آخرین ورود')),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('customer_type', models.CharField(choices=[('retail', 'مشتری خرد'), ('wholesale', 'مشتری عمده'), ('admin', 'ادمین سایت')], default='retail', max_length=10, verbose_name='نوع کاربر')),
                ('is_hurry', models.BooleanField(default=False, verbose_name='خرید همکار به صورت فوری')),
                ('store_phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='تلفن فروشگاه')),
                ('store_card', models.ImageField(blank=True, null=True, upload_to='financial_documents/', verbose_name='تصویر کارت فروشگاه')),
                ('photo_of_the_store', models.ImageField(blank=True, null=True, upload_to='financial_documents/', verbose_name='تصویر فروشگاه')),
                ('business_license', models.ImageField(blank=True, null=True, upload_to='financial_documents/', verbose_name='تصویر مجوز تجاری')),
                ('groups', models.ManyToManyField(blank=True, related_name='groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='permissions', to='auth.permission')),
            ],
            options={
                'verbose_name_plural': 'کاربران',
            },
        ),
    ]

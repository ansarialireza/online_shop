# Generated by Django 4.2.5 on 2024-01-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cornicesize',
            name='price',
        ),
        migrations.RemoveField(
            model_name='cornicesupply',
            name='price',
        ),
        migrations.AddField(
            model_name='cornicesize',
            name='price_retail',
            field=models.IntegerField(default=1, verbose_name='قیمت خرده'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cornicesize',
            name='price_wholesale',
            field=models.IntegerField(default=1, verbose_name='قیمت عمده'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cornicesupply',
            name='price_retail',
            field=models.IntegerField(default=1, verbose_name='قیمت خرده'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cornicesupply',
            name='price_wholesale',
            field=models.IntegerField(default=1, verbose_name='قیمت عمده'),
            preserve_default=False,
        ),
    ]
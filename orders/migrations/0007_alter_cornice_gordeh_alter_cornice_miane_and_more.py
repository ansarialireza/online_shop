# Generated by Django 4.2.5 on 2024-02-03 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_orderitem_gordeh_remove_orderitem_miane_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cornice',
            name='Gordeh',
            field=models.CharField(blank=True, default=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cornice',
            name='Miane',
            field=models.CharField(blank=True, default=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cornice',
            name='Scouti',
            field=models.CharField(blank=True, default=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cornice',
            name='Tasho',
            field=models.CharField(blank=True, default=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cornice',
            name='cornice_7',
            field=models.CharField(blank=True, default=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cornice',
            name='cornice_9',
            field=models.CharField(blank=True, default=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='floorcoverings',
            name='glue_10kg',
            field=models.CharField(blank=True, default=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='floorcoverings',
            name='glue_4kg',
            field=models.CharField(blank=True, default=False, max_length=255, null=True),
        ),
    ]
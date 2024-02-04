# Generated by Django 4.2.5 on 2024-02-03 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_cornice_gordeh_alter_cornice_miane_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cornice',
            name='Gordeh',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cornice',
            name='Miane',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cornice',
            name='Scouti',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cornice',
            name='Tasho',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cornice',
            name='cornice_7',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cornice',
            name='cornice_9',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='floorcoverings',
            name='glue_10kg',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='floorcoverings',
            name='glue_4kg',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]

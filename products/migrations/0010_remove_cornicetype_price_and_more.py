# Generated by Django 4.2.5 on 2024-02-02 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_cornicetype_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cornicetype',
            name='price',
        ),
        migrations.RemoveField(
            model_name='cornice',
            name='cornicesupply',
        ),
        migrations.AddField(
            model_name='cornice',
            name='Gordeh',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, related_name='Gordeh', to='products.price', verbose_name='(پایان کار) گرده'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cornice',
            name='Miane',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='Miane', to='products.price', verbose_name='میانه'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cornice',
            name='Scouti',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='Scouti', to='products.price', verbose_name='اسکوتیا'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cornice',
            name='Tasho',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, related_name='Tasho', to='products.price', verbose_name='تاشو'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cornice',
            name='Cornic_7',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cornices_7', to='products.price', verbose_name='قرنیز 7 سانتی'),
        ),
        migrations.AlterField(
            model_name='cornice',
            name='Cornice_9',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cornices_9', to='products.price', verbose_name='قرنیز 9 سانتی'),
        ),
        migrations.DeleteModel(
            name='CorniceSupply',
        ),
        migrations.DeleteModel(
            name='CorniceType',
        ),
    ]

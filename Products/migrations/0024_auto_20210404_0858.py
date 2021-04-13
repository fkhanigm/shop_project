# Generated by Django 3.1.5 on 2021-04-04 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0023_auto_20210217_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='off',
            name='shop_product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Off', related_query_name='Off', to='Products.shopproduct', verbose_name='Shop_product'),
        ),
    ]
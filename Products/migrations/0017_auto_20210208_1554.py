# Generated by Django 3.1.5 on 2021-02-08 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0016_auto_20210206_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='color name')),
                ('code', models.CharField(max_length=50, verbose_name='color code')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='product name')),
                ('code', models.CharField(max_length=50, verbose_name='size code')),
            ],
        ),
        migrations.AddField(
            model_name='shopproduct',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ShopProduct', related_query_name='ShopProduct', to='Products.color', verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='shopproduct',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ShopProduct', related_query_name='ShopProduct', to='Products.size', verbose_name='Size'),
        ),
    ]

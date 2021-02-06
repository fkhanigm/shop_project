# Generated by Django 3.1.5 on 2021-01-27 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0002_auto_20210127_0553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('rate', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Products/images/images', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('publish_time', models.DateTimeField(db_index=True, verbose_name='Publish at')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.RemoveField(
            model_name='images',
            name='product',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='off',
            options={'verbose_name': 'Off', 'verbose_name_plural': 'Offes'},
        ),
        migrations.AlterModelOptions(
            name='productmeta',
            options={'verbose_name': 'ProductMeta', 'verbose_name_plural': 'ProductMetas'},
        ),
        migrations.AlterModelOptions(
            name='shopproduct',
            options={'verbose_name': 'ShopProduct', 'verbose_name_plural': 'ShopProducts'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='details',
            new_name='detail',
        ),
        migrations.RemoveField(
            model_name='like',
            name='products',
        ),
        migrations.AddField(
            model_name='like',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Like', related_query_name='Likes', to='Products.product', verbose_name='Product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Like', related_query_name='Likes', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product', related_query_name='Product', to='Products.brand', verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product', related_query_name='Product', to='Products.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='productmeta',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductMeta', related_query_name='ProductMeta', to='Products.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ShopProduct', related_query_name='ShopProduct', to='Products.product', verbose_name='Product'),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Images', related_query_name='Image', to='Products.product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment', related_query_name='Comments', to='Products.product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment', related_query_name='Comments', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
# Generated by Django 3.1.5 on 2021-05-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0046_auto_20210516_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='Products/images/images', verbose_name='Image'),
        ),
    ]

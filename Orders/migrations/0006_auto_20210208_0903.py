# Generated by Django 3.1.5 on 2021-02-08 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0005_auto_20210208_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='ordered',
            field=models.BooleanField(default=False, verbose_name='Ordered'),
        ),
        migrations.AddField(
            model_name='basketitems',
            name='ordered',
            field=models.BooleanField(default=False, verbose_name='Ordered'),
        ),
    ]
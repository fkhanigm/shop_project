# Generated by Django 3.1.5 on 2021-02-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0003_auto_20210207_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitems',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]

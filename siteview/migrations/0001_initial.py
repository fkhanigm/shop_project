# Generated by Django 3.1.5 on 2021-05-26 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstSlideIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='siteview/firstslideindex/images', verbose_name='image')),
                ('title_one', models.CharField(max_length=500, verbose_name='product title one')),
                ('title_two', models.CharField(max_length=500, verbose_name='product title two')),
                ('detail', models.CharField(max_length=500, verbose_name='product detail')),
                ('draft', models.BooleanField(db_index=True, default=True, verbose_name='Draft')),
            ],
            options={
                'verbose_name': 'FirstSlideIndex',
                'verbose_name_plural': 'FirstSlideIndex',
            },
        ),
    ]

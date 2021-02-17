# Generated by Django 3.1.5 on 2021-02-06 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_auto_20210206_0719'),
        ('Products', '0012_auto_20210206_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='off',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, related_name='Off', related_query_name='Off', to='Accounts.shop', verbose_name='Shop'),
        ),
    ]

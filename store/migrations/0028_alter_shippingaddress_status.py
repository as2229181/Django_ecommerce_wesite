# Generated by Django 3.2.18 on 2023-06-11 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_auto_20230610_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 4.2.1 on 2023-06-20 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Delivery', '0002_alter_delivery_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='order_status',
            field=models.CharField(max_length=32),
        ),
    ]

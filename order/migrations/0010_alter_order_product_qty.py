# Generated by Django 4.2.2 on 2023-07-03 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_order_product_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_qty',
            field=models.PositiveIntegerField(),
        ),
    ]

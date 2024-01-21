# Generated by Django 4.2.2 on 2023-09-27 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_alter_checkout_status_alter_checkoutitem_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutitem',
            name='color',
            field=models.CharField(choices=[('Blue', 'Blue'), ('Red', 'Red'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Brown', 'Brown'), ('Pink', 'Pink'), ('White', 'White'), ('Black', 'Black')], max_length=20, null=True, verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='checkoutitem',
            name='size',
            field=models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=10, null=True, verbose_name='Size'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-20 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_productimage_options_product_prod_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(verbose_name='Slug'),
        ),
    ]

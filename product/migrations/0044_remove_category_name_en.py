# Generated by Django 4.2.2 on 2024-02-08 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0043_category_name_en'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name_en',
        ),
    ]

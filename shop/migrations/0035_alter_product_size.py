# Generated by Django 4.2.6 on 2023-12-13 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0034_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(to='shop.size'),
        ),
    ]

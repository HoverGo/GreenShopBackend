# Generated by Django 4.2.6 on 2023-11-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_product_mainprice_alter_product_saleprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mainPrice',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='salePrice',
            field=models.FloatField(editable=False),
        ),
    ]

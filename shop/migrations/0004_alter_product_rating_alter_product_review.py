# Generated by Django 4.2.6 on 2023-11-06 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_saleprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.IntegerField(default=0),
        ),
    ]

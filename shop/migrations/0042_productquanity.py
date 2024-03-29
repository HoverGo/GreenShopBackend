# Generated by Django 4.2.6 on 2023-12-22 17:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0041_alter_order_shippingprice_alter_order_subtotalprice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductQuanity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.size')),
            ],
        ),
    ]

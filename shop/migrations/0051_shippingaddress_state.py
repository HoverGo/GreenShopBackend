# Generated by Django 4.2.6 on 2023-12-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0050_alter_shippingaddress_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='state',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
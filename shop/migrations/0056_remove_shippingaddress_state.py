# Generated by Django 4.2.6 on 2023-12-29 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0055_alter_shippingaddress_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='state',
        ),
    ]

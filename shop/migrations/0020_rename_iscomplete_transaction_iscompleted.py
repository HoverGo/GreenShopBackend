# Generated by Django 4.2.6 on 2023-11-21 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_remove_shippingaddress_order_order_shippingaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='isComplete',
            new_name='isCompleted',
        ),
    ]

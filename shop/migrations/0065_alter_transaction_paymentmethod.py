# Generated by Django 4.2.6 on 2024-01-06 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0064_transaction_paymentmethod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='paymentMethod',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.paymentmethod'),
        ),
    ]

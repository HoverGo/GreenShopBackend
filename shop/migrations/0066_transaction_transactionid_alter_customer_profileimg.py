# Generated by Django 4.2.6 on 2024-01-06 21:44

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0065_alter_transaction_paymentmethod'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transactionId',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='profileImg',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.upload_to),
        ),
    ]

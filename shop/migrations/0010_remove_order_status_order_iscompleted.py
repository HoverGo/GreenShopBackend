# Generated by Django 4.2.6 on 2023-11-16 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_customer_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='isCompleted',
            field=models.BooleanField(default=False),
        ),
    ]

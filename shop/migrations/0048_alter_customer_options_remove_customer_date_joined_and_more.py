# Generated by Django 4.2.6 on 2023-12-28 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0047_alter_customer_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.RemoveField(
            model_name='customer',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
    ]
